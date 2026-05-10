#Josephine Greiff
#CIT-119
#Final Project Contact Manager
#This program is a simple contact manager that allows user to add, view, search, and delete a contact.
#The program stores the contact data in a SQLite database so the information can then be saved and reused.

import sqlite3

DATABASE_NAME = "contacts.db"

def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
        (name, phone, email)
    )

    conn.commit()
    conn.close()
    print("Contact added successfully.")

def view_contacts():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    conn.close()
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        print("\nContact List")
        print("------------")
        for contact in contacts:
            print("ID:", contact[0])
            print("Name:", contact[1])
            print("Phone:", contact[2])
            print("Email:", contact[3])
            print()

def search_contact():
    search_name = input("Enter the name to search for: ")

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ("%" + search_name + "%",))
    contacts = cursor.fetchall()
    conn.close()
    if len(contacts) == 0:
        print("No matching contacts found.")
    else:
        print("\nSearch Results")
        print("--------------")
        for contact in contacts:
            print("ID:", contact[0])
            print("Name:", contact[1])
            print("Phone:", contact[2])
            print("Email:", contact[3])
            print()

def delete_contact():
    view_contacts()
    contact_id = input("Enter the ID of the contact to delete: ")
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()
    print("Contact deleted if the ID existed.")

def show_menu():
    print("\nContact Manager")
    print("---------------")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    create_database()
    choice = ""
    while choice != "5":
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye.")
        else:
            print("Invalid choice. Please choose 1-5.")

main()
