import re
import json
import sys

# Data storage
contacts = {}
#Define UI Menu
def display_welcome_message():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")
#Added email validation using re.match()
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)
#Added phone number validation using re.match()
def validate_phone(phone):
    pattern = r'^\+?[1-9]\d{1,14}$'  # E.164 format
    return re.match(pattern, phone)
#Add a new contact
def add_contact():
    try:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        if not validate_phone(phone):
            print("Invalid phone number format.")
            return
        email = input("Enter email address: ")
        if not validate_email(email):
            print("Invalid email format.")
            return
        address = input("Enter address (optional): ")
        notes = input("Enter additional notes (optional): ")
        
        if phone in contacts:
            print("A contact with this phone number already exists.")
            return
        
        contacts[phone] = {
            "name": name,
            "email": email,
            "address": address,
            "notes": notes
        }
        print("Contact added successfully!")

    except Exception as e:
        print(f"An error occurred while adding contact: {e}")
#Edit contact information
def edit_contact():
    try:
        phone = input("Enter the phone number of the contact to edit: ")
        if phone not in contacts:
            print("Contact not found.")
            return
        
        name = input("Enter new name (leave blank to keep current): ")
        email = input("Enter new email address (leave blank to keep current): ")
        address = input("Enter new address (leave blank to keep current): ")
        notes = input("Enter new notes (leave blank to keep current): ")

        if name:
            contacts[phone]["name"] = name
        if email and validate_email(email):
            contacts[phone]["email"] = email
        if address:
            contacts[phone]["address"] = address
        if notes:
            contacts[phone]["notes"] = notes
        
        print("Contact updated successfully!")

    except Exception as e:
        print(f"An error occurred while editing contact: {e}")
#remove contact
def delete_contact():
    try:
        phone = input("Enter the phone number of the contact to delete: ")
        if phone in contacts:
            del contacts[phone]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")
    
    except Exception as e:
        print(f"An error occurred while deleting contact: {e}")
#add search contacts by phone number
def search_contact():
    try:
        phone = input("Enter the phone number of the contact to search: ")
        if phone in contacts:
            contact = contacts[phone]
            print(f"Contact found: {contact}")
        else:
            print("Contact not found.")
    
    except Exception as e:
        print(f"An error occurred while searching for contact: {e}")
#display all contacts
def display_contacts():
    try:
        if not contacts:
            print("No contacts available.")
            return
        for phone, details in contacts.items():
            print(f"Phone: {phone}, Details: {details}")

    except Exception as e:
        print(f"An error occurred while displaying contacts: {e}")
#BONUS: Export to a text file/input via a text file
def export_contacts():
    try:
        with open('contacts.txt', 'w') as f:
            json.dump(contacts, f, indent=4)
        print("Contacts exported successfully!")

    except Exception as e:
        print(f"An error occurred while exporting contacts: {e}")

def import_contacts():
    try:
        with open('contacts.txt', 'r') as f:
            imported_contacts = json.load(f)
            contacts.update(imported_contacts)
            print("Contacts imported successfully!")

    except FileNotFoundError:
        print("No export file found.")
    except Exception as e:
        print(f"An error occurred while importing contacts: {e}")

def main():
    while True:
        display_welcome_message()
        choice = input("Please choose an option (1-8): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please choose a number between 1 and 8.")

if __name__ == "__main__":
    main()

