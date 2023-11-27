import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = []
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts, name, phone, email, address):
    new_contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact(contacts, search_term):
    results = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    return results

def update_contact(contacts, contact_index, name, phone, email, address):
    if 0 < contact_index <= len(contacts):
        contacts[contact_index - 1] = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        save_contacts(contacts)
        print(f"Contact '{name}' updated successfully.")
    else:
        print("Invalid contact index.")

def delete_contact(contacts, contact_index):
    if 0 < contact_index <= len(contacts):
        removed_contact = contacts.pop(contact_index - 1)
        save_contacts(contacts)
        print(f"Contact '{removed_contact['name']}' deleted successfully.")
    else:
        print("Invalid contact index.")

def main():
    contacts = load_contacts()

    while True:
        print("\n==== Contact Management System ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            address = input("Enter contact address: ")
            add_contact(contacts, name, phone, email, address)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_term = input("Enter search term (name or phone number): ")
            search_results = search_contact(contacts, search_term)
            view_contacts(search_results)
        elif choice == '4':
            view_contacts(contacts)
            contact_index = int(input("Enter the contact index to update: "))
            name = input("Enter updated name: ")
            phone = input("Enter updated phone number: ")
            email = input("Enter updated email: ")
            address = input("Enter updated address: ")
            update_contact(contacts, contact_index, name, phone, email, address)
        elif choice == '5':
            view_contacts(contacts)
            contact_index = int(input("Enter the contact index to delete: "))
            delete_contact(contacts, contact_index)
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
