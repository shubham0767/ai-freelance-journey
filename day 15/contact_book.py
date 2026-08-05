print("=" * 40)
print("Contact Book")
print("=" * 40)

contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        print("Contact Added Successfully!")

    elif choice == "2":
        name = input("Enter Name to Search: ")

        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact Not Found!")

    elif choice == "3":
        print("\nAll Contacts")

        if len(contacts) == 0:
            print("No Contacts Available.")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")