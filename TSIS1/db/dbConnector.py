import psycopg2
from config.config import load_config
from db.PhoneBook import PhoneBook


class DBConnector:
    def __init__(self):
        self.config = load_config()
        

    def createTable(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS groups (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        );

        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            email VARCHAR(100),
            birthday DATE,
            group_id INTEGER REFERENCES groups(id)
        );

        CREATE TABLE IF NOT EXISTS phones (
            id SERIAL PRIMARY KEY,
            contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
            phone VARCHAR(20),
            type VARCHAR(10) CHECK (type IN ('home','work','mobile'))
        );
        '''
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                conn.commit()
        except Exception as e:
            print("Error:", e)

    
    def getAllRecords(self):
        sql = """
        SELECT c.id, c.first_name, c.last_name, c.email, c.birthday, g.name,
               p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        ORDER BY c.id
        """
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    rows = cur.fetchall()

                    contacts = {}

                    for row in rows:
                        cid = row[0]

                        if cid not in contacts:
                            contacts[cid] = {
                                "id": cid,
                                "first_name": row[1],
                                "last_name": row[2],
                                "email": row[3],
                                "birthday": row[4],
                                "group": row[5],
                                "phones": []
                            }

                        if row[6]:
                            contacts[cid]["phones"].append((row[6], row[7]))

                    return list(contacts.values())

        except Exception as e:
            print("Error:", e)

    
    def addContact(self, user: PhoneBook):
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:

                    # group
                    cur.execute("""
                        INSERT INTO groups(name)
                        VALUES(%s)
                        ON CONFLICT (name) DO NOTHING
                    """, (user.group,))

                    cur.execute("SELECT id FROM groups WHERE name=%s", (user.group,))
                    group_id = cur.fetchone()[0]

                    # contact
                    cur.execute("""
                        INSERT INTO contacts(first_name, last_name, email, birthday, group_id)
                        VALUES(%s, %s, %s, %s, %s)
                        RETURNING id
                    """, (user.first_name, user.last_name, user.email, user.birthday, group_id))

                    contact_id = cur.fetchone()[0]

                    # phones
                    for phone, ptype in user.phones:
                        cur.execute("""
                            INSERT INTO phones(contact_id, phone, type)
                            VALUES(%s, %s, %s)
                        """, (contact_id, phone, ptype))

                conn.commit()

        except Exception as e:
            print("Error:", e)

    
    def getLimitOffset(self, limit, offset):
        sql = """
        SELECT c.first_name, c.last_name, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LIMIT %s OFFSET %s
        """
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (limit, offset))
                    return cur.fetchall()
        except Exception as e:
            print("Error:", e)

    
    def deleteUserByFirstName(self, first_name):
        sql = "DELETE FROM contacts WHERE first_name=%s"
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (first_name,))
                conn.commit()
        except Exception as e:
            print("Error:", e)

    
    def searchByEmail(self, query):
        sql = """
        SELECT first_name, last_name, email
        FROM contacts
        WHERE email ILIKE %s
        """
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (f"%{query}%",))
                    return cur.fetchall()
        except Exception as e:
            print("Error:", e)

    
    def filterByGroup(self, group_name):
        sql = """
        SELECT c.first_name, c.last_name, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
        """
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (group_name,))
                    return cur.fetchall()
        except Exception as e:
            print("Error:", e)

    
    def sortContacts(self, field):
        if field not in ["first_name", "birthday"]:
            print("Invalid sort field")
            return []

        sql = f"""
        SELECT first_name, last_name, email, birthday
        FROM contacts
        ORDER BY {field}
        """

        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    return cur.fetchall()
        except Exception as e:
            print("Error:", e)
            
    