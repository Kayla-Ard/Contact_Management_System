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
    #DONE!      # Contact Categories (Bonus):
    #DONE!      # Implement the ability to categorize contacts into groups (e.g., friends, family, work). Each contact can belong to one or more categories.
    #DONE!      # Contact Search (Bonus): DONE!
                # Enhance the contact search functionality to allow users to search for contacts by name, phone number, email address, or additional information.
    # Contact Sorting (Bonus):
        # Implement sorting options to display contacts alphabetically by name or based on other criteria.
    # Backup and Restore (Bonus):
        # Add features to create automatic backups of contact data and the ability to restore data from a backup file.
    # DONE!     # Custom Contact Fields (Bonus):
                # Allow users to define custom fields for contacts (e.g., birthdays, anniversaries) and store this information.


import re

def add_contact(contacts):
    email = input("Enter a valid email address for the contact you would like to add: ").lower()
    matched_email = re.match(r"\b[A-Za-z0-9À-ÿ._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b", email)
    print(matched_email)
    if matched_email:
        print("Valid email")
        if email not in contacts:
            print("Email added successfully")
            first_name = input('Enter the first name of the contact you would like to add: ').title()
            if first_name.isalpha() == True:   
                print("First name stored successfully")
                last_name = input('Enter the last name of the contact you would like to add: ').title()
                if last_name.isalpha() == True:
                    print("Last name stored successfully")
                    name = first_name + ' ' + last_name
                else: 
                    print("Invalid name entry")
            else: 
                print("Invalid name entry")

            phone_number = input('Enter the phone number (separated only by a dash - Example "123-456-7890")) of the contact you would like to add: ')
            verified_phone_number = re.match(r"\d{3}-\d{3}-\d{4}", phone_number)
            if verified_phone_number:
                print("Valid phone number")
            else:
                print("Invalid phone number")
                
            category = input("""Assign this contact to a category by entering a number from the menu below: 
                
                Category Menu:
                    1 - Friend
                    2 - Family
                    3 - Work
                    """)
            if category == "1":
                category = "Friend"
                print("Contact was successfully stored as a friend")
            elif category == "2":
                category = "Family"
                print("Contact was successfully stored as a family member")
            elif category == "3":
                category = "Work"
                print("Contact was successfully stored as a work colleague")
            else:
                print("You entered an invalid choice")
                
            custom_field_option = input('Would you like to add a custom field to this contact? Enter "yes" or "no: "').lower()
            if custom_field_option == "yes":
                custom_field_category = input("Enter the custom field category would you like to add? (Examples: Anniversary, Birthday): ").title()
                custom_field = input(f"Enter the custom field you would like to assign to {custom_field_category}: ").title()
                print(f"{custom_field} was successfully stored under {custom_field_option}")
            
            elif custom_field_option == "no": 
                custom_field_category = "Custom Field Category"
                custom_field = "None"
                print('This contact will be stored with a "Custom Field Category" of "None", incase you would ever like to add one')
            
            else:
                print("You entered an invalid choice")
            
            contacts[email] = {"Name": name, "Phone Number": phone_number, "Category": category, custom_field_category: custom_field}
            print(f"Here is your current list of contacts: \n{contacts}")
        else:
            print("That email is already being used in contacts")
    else:
        print("Invalid email")

def edit_contact(contacts):
    email = input("Enter the email address for the contact you would like to make changes to: ").lower()
    if email in contacts:
        edit = input('Would you like to edit the name or the phone number? Enter "1" for name or "2" for phone number": ')
        if edit == "1":
            first_name_update = input('Enter the first name you would like the first name changed to: ').title()
            if first_name_update.isalpha() == True:
                print("Valid first name")
                last_name_update = input('Enter the last name of the contact you would like the last name changed to: ').title()
                if last_name_update.isalpha() == True:
                    print("Valid last name")
                    name_update = first_name_update + last_name_update
                    print(f"The name has been updated. Here is your updated list of contacts: \n{contacts}")
                else: 
                    print("Invalid name entry")
                    contacts[email]["Name"] = name_update
                    print("Name updated")
            else: 
                print("Invalid name entry")
        elif edit == "2":
            number_update = input('Enter the phone number (separated only by dashes - Example "123-456-7890") you would like the phone number changed to: ')
            verified_phone_number = re.match(r"\d{3}-\d{3}-\d{4}", number_update)
            if verified_phone_number:
                print("Valid phone number") 
                contacts[email]["Phone Number"] = number_update
                print(f"The phone number has been updated. Here is your updated list of contacts: \n{contacts}")
            else:
                print("Invalid phone number entry")
        else:
            print("Invalid entry")
    else:
        print("The email you entered does not match any of the contacts")     
    
def delete_contact(contacts): 
    email = input("Enter the email address for the contact you would like to delete: ").lower()
    if email in contacts:
        del contacts[email]
        print(f"The contact has been deleted. Here is your updated list of contacts: \n{contacts}")
    else:
        print("The email you entered does not match any of the contacts")
            
def search_contact(contacts): 
    search_choice = input("""Choose how you would like to search for a contact by entering a number from the menu below: 
                
                Category Menu:
                    1 - Email
                    2 - Name 
                    3 - Phone Number
                    """)
    
    if search_choice == "1":
        email = input("Enter the email address for the contact you would like to search: ").lower()
        if email in contacts:
            print(f"Here is contact you searched for: \n{contacts[email]}")
        else:
            print("The email you entered does not match any of the contacts")
            
    elif search_choice == "2": # NOT WORKING
        name = input('Enter the full name of the contact you would like to search: ').title()
        if name in contacts[email]["Name"] == name:
            print(f"Here is contact you searched for: \n{contacts[email][name]}")
        else:
            print("The name you entered does not match any of the contacts")
            
    elif search_choice == "3": # NOT WORKING
        phone_number = input('Enter the phone number (separated only by a dash - Example "123-456-7890")) of the contact you would like to search: ')
        verified_phone_number = re.match(r"\d{3}-\d{3}-\d{4}", phone_number)
        if verified_phone_number in contacts[email]["Phone Number"]:
            print(f"Here is the contact you searched for: \n{contacts[email]}")
        else:
            print("The phone number you entered does not match any of the contacts")
    
    else:
        print("You entered an invalid choice")

def display_contacts(contacts): #BETTER FORMAT TO PRINT THIS IN SO ITS EASIER TO READ?
    sorted_contacts = dict(
    sorted(contacts.items(), key=lambda item: item[1]['Name']))
    print(f"Here are all the contacts that are currently stored in alphabetical order according to first name: \n{sorted_contacts}")   

def export_contact(contacts):
    my_contacts = contacts
    with open("contacts.txt", "w") as file:
        for email, name in my_contacts.items():
            file.write(f"{email}:\n")
            for contact_info, number in name.items():
                file.write(f"   {contact_info}: {number}\n")           

def import_contact(): 
    my_contacts = {}
    with open("my_contacts.txt", "r") as file:
        for line in file:
            email, first_name, last_name, phone_number = line.strip().split("  ")
            my_contacts = {f"{email} {first_name} {last_name} {phone_number}"}
    print(my_contacts)

def contact_management_system():
    contacts_info = {}
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
            add_contact(contacts_info)
            
        elif menu_choice == "2":
            edit_contact(contacts_info)
            
        elif menu_choice == "3":
            delete_contact(contacts_info)
            
        elif menu_choice == "4":
            search_contact(contacts_info)
            
        elif menu_choice == "5":
            display_contacts(contacts_info)
            
        elif menu_choice == "6":
            export_contact(contacts_info)
            
        elif menu_choice == "7":
            import_contact()
            
        elif menu_choice == "8":
            print("Thanks for using the Contact Management System! Good-bye!")
            break
        
        else:
            print("You entered an invalid choice")

contact_management_system()