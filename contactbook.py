contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def view_contacts():
    for name, phone in contacts.items():
        print(f"Name: {name}, Phone: {phone}")

def search_contact(name):
    if name in contacts:
        print(f"Found: {name}, Phone: {contacts[name]}")
    else:
        print("Contact not found.")

def contact_book():
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

contact_book()
