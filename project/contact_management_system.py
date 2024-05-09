# Module 3: Mini-Project | Contact Management System
# Project Requirements
# Your task is to develop a Contact Management System with the following features:
# 1. User Interface (UI):
    # Create a user-friendly command-line interface (CLI) for the Contact Management System.
    # Display a welcoming message and provide a menu with the following options:
    # ``` Welcome to the Contact Management System! Menu:
    # Add a new contact
    # Edit an existing contact
    # Delete a contact
    # Search for a contact
    # Display all contacts
    # Export contacts to a text file
    # Import contacts from a text file *BONUS
    # Quit "> 

# 2. Contact Data Storage:
    # Use nested dictionaries as the main data structure for storing contact information.
    # Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
    # Store contact details within the inner dictionary, including:
    # Name
    # Phone number
    # Email address
    # Additional information (e.g., address, notes).
    
# 3. Menu Actions:
    # Implement the following actions in response to menu selections:
    # Adding a new contact with all relevant details.
    # Editing an existing contact's information (name, phone number, email, etc.).
    # Deleting a contact by searching for their unique identifier.
    # Searching for a contact by their unique identifier and displaying their details.
    # Displaying a list of all contacts with their unique identifiers.
    # Exporting contacts to a text file in a structured format.
    # Importing contacts from a text file and adding them to the system. * BONUS
    
# 4. User Interaction:
    # Utilize input() to enable users to select menu options and provide contact details.
    # Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.

# 5. Error Handling:
    # Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.


# Optional Bonus Points
    # Contact Categories (Bonus):
        # Implement the ability to categorize contacts into groups (e.g., friends, family, work). Each contact can belong to one or more categories.
    # Contact Search (Bonus):
        # Enhance the contact search functionality to allow users to search for contacts by name, phone number, email address, or additional information.
    # Contact Sorting (Bonus):
        # Implement sorting options to display contacts alphabetically by name or based on other criteria.
    # Backup and Restore (Bonus):
        # Add features to create automatic backups of contact data and the ability to restore data from a backup file.
    # Custom Contact Fields (Bonus):
        # Allow users to define custom fields for contacts (e.g., birthdays, anniversaries) and store this information.

# ``` Welcome to the Contact Management System! Menu:
# Add a new contact
# Edit an existing contact
# Delete a contact
# Search for a contact
# Display all contacts
# Export contacts to a text file
# Import contacts from a text file *BONUS
# Quit "> 


import re

contacts = {}

def add_contact():
    email = input("Enter a valid email address for the contact you would like to add: ")
    matched_email = re.match(r"\b[A-Za-z0-9À-ÿ._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b", email)
    print(matched_email)
    if matched_email:
        print("Valid email")
    else:
        print("Invalid email")
    
    name = input('Enter the first and last name (separated only by a space - Example "John Doe")) of the contact you would like to add: ')
    if name.isalpha() == True:
        print("Named stored")
    else: 
        print("Invalid name entry")

    phone_number = input('Enter the phone number (separated only by a dash - Example "123-456-7890")) of the contact you would like to add: ')
    pass
    
    contacts[email] = {"Name": name, "Phone Number": phone_number}

def edit_contact():
    pass

def delete_contact():
    pass

def search_contact():
    pass

def display_contact():
    pass

def export_contact():
    pass

def import_contact():
    pass


def contact_management_system():
    print("Welcome to the Contact Management System!")
    while True: 
        menu_choice = input("""Please select an option below from the menu by entering the number assigned to your desired choice: 
            Menu:
                1 - Add a new contact
                2 - Edit an existing contact
                3 - Delete a contact
                4 - Search for a contact
                5 - Display all contacts
                6 - Export contacts to a text file
                7 - Import contacts from a text file
                8 - Quit         
            """)
        if menu_choice == "1":
            pass
        elif menu_choice == "2":
            pass
        elif menu_choice == "3":
            pass
        elif menu_choice == "4":
            pass
        elif menu_choice == "5":
            pass
        elif menu_choice == "6":
            pass
        elif menu_choice == "7":
            pass
        elif menu_choice == "8":
            print("Thanks for using the Contact Management System! Good-bye!")
            break
        else:
            print("You entered an invalid choice")
contact_management_system()