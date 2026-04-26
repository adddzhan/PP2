from db.dbConnector import DBConnector
from db.PhoneBook import PhoneBook

db = DBConnector()
db.createTable()

while True:
    print("\n[1] GET ALL CONTACTS")
    print("[2] ADD CONTACT")
    print("[3] GET BY LIMIT/OFFSET")
    print("[4] DELETE BY NAME")
    print("[0] EXIT")

    choice = int(input("Choose: "))

    if choice == 0:
        break

    # 🔹 GET ALL
    elif choice == 1:
        data = db.getAllRecords()
        for user in data:
            print(user)

    # 🔹 ADD CONTACT
    elif choice == 2:
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        birthday = input("Birthday (YYYY-MM-DD): ")
        group = input("Group (Family/Friend/Work): ")

        # телефоны
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

    # 🔹 PAGINATION
    elif choice == 3:
        limit = int(input("Limit: "))
        offset = int(input("Offset: "))
        data = db.getLimitOffset(limit, offset)
        for row in data:
            print(row)

    # 🔹 DELETE
    elif choice == 4:
        name = input("Enter first name: ")
        db.deleteUserByFirstName(name)
        print("✅ Deleted")