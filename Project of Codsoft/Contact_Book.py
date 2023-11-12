class Contact:
    def __init__(self, store_name, phone_number, email, address):
        self.store_name = store_name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Store Name: {contact.store_name}, Phone Number: {contact.phone_number}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.store_name == name:
                return contact
        return None

    def update_contact(self, name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.store_name == name:
                self.contacts[i] = new_contact

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.store_name != name]

# User interface
contact_list = ContactList()

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        store_name = input("Enter Store Name: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        contact_list.add_contact(Contact(store_name, phone_number, email, address))
    elif choice == 2:
        contact_list.view_contacts()
    elif choice == 3:
        name = input("Enter Store Name to Search: ")
        contact = contact_list.search_contact(name)
        if contact:
            print(f"Store Name: {contact.store_name}, Phone Number: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("Contact not found.")
    elif choice == 4:
        name = input("Enter Store Name to Update: ")
        store_name = input("Enter New Store Name: ")
        phone_number = input("Enter New Phone Number: ")
        email = input("Enter New Email: ")
        address = input("Enter New Address: ")
        contact_list.update_contact(name, Contact(store_name, phone_number, email, address))
    elif choice == 5:
        name = input("Enter Store Name to Delete: ")
        contact_list.delete_contact(name)
    elif choice == 6:
        break
