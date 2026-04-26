from db.dbConnector import DBConnector
from db.PhoneBook import PhoneBook

db = DBConnector()
db.createTable()

while True:
    print("\n[1] GET ALL CONTACTS")
    print("[2] ADD CONTACT")
    print("[3] PAGINATION (NEXT/PREV)")
    print("[4] DELETE BY NAME")
    print("[5] SEARCH BY EMAIL")
    print("[6] FILTER BY GROUP")
    print("[7] SORT CONTACTS")
    print("[0] EXIT")

    choice = int(input("Choose: "))

    if choice == 0:
        break

    
    elif choice == 1:
        data = db.getAllRecords()
        for user in data:
            if data:
                for user in data:
                    print(user)
            else:
                print("No data or DB error")
                
    

    
    elif choice == 2:
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        birthday = input("Birthday (YYYY-MM-DD): ")
        group = input("Group (Family/Friend/Work): ")

        phones = []
        count = int(input("How many phones? "))

        for i in range(count):
            phone = input("Phone: ")
            ptype = input("Type (home/work/mobile): ")
            phones.append((phone, ptype))

        user = PhoneBook(
            id=0,
            first_name=first_name,
            last_name=last_name,
            email=email,
            birthday=birthday,
            group=group,
            phones=phones
        )

        db.addContact(user)
        print("✅ Contact added")

    
    elif choice == 3:
        limit = int(input("Enter limit: "))
        offset = 0

        while True:
            data = db.getLimitOffset(limit, offset)

            if not data:
                print("No more records")
                break

            for row in data:
                print(row)

            action = input("next / prev / quit: ")

            if action == "next":
                offset += limit
            elif action == "prev":
                offset = max(0, offset - limit)
            elif action == "quit":
                break

    
    elif choice == 4:
        name = input("Enter first name: ")
        db.deleteUserByFirstName(name)
        print("✅ Deleted")

    
    elif choice == 5:
        query = input("Enter email keyword: ")
        results = db.searchByEmail(query)
        for r in results:
            print(r)

    
    elif choice == 6:
        group = input("Enter group (Family/Friend/Work): ")
        results = db.filterByGroup(group)
        for r in results:
            print(r)

    
    elif choice == 7:
        field = input("Sort by (first_name/birthday): ")
        results = db.sortContacts(field)
        for r in results:
            print(r)