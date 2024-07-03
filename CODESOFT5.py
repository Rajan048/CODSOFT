import json

# Define the contact book as a dictionary
contacts = {}

def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

def load_contacts():
    global contacts
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    if name in contacts:
        print("Contact already exists.")
        return
    number = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter home address: ")
    contacts[name] = {"number": number, "email": email, "address": address}
    save_contacts()
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    for name, details in contacts.items():
        print(f"Name: {name}, Phone Number: {details['number']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    for name, details in contacts.items():
        if search_term in name or search_term in details['number']:
            print(f"Name: {name}, Phone Number: {details['number']}, Email: {details['email']}, Address: {details['address']}")
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name not in contacts:
        print("Contact not found.")
        return
    print(f"Updating details for {name}. Leave field empty to keep current value.")
    number = input(f"Enter new phone number ({contacts[name]['number']}): ") or contacts[name]['number']
    email = input(f"Enter new email address ({contacts[name]['email']}): ") or contacts[name]['email']
    address = input(f"Enter new home address ({contacts[name]['address']}): ") or contacts[name]['address']
    contacts[name] = {"number": number, "email": email, "address": address}
    save_contacts()
    print("Contact updated successfully.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts()
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def display_menu():
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    load_contacts()
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the contact book application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
