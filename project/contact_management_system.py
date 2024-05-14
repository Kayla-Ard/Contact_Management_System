# Module 3: Mini-Project | Contact Management System
    

# 5. Error Handling:
    # Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.

# Create a clean and interactive README.md file in your GitHub repository.
# Include clear instructions on how to run the application and explanations of its features.
# Provide examples and screenshots, if possible, to enhance user understanding.
# Include a link to your GitHub repository in your project documentation.


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
        edit = input('''What would you like to edit? Select an option from the menu below:
                     Edit Contact Menu:
                    1 - Email
                    2 - Name 
                    3 - Phone Number
                    4 - Category
                    5 - Custom Field Category
                     ''')
        if edit == "1":
            email_update = input("Enter a valid email address to update the contact: ").lower()
            matched_email = re.match(r"\b[A-Za-z0-9À-ÿ._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b", email_update)
            if matched_email:
                contacts[email_update] = contacts[email]
                del contacts[email]
                print(f"The email has been updated. Here is your updated list of contacts: \n{contacts}")
            else:
                print("The email you entered does not match any of the contacts")       
        
        elif edit == "2":
            first_name_update = input('Enter the first name you would like the first name changed to: ').title()
            if first_name_update.isalpha() == True:
                print("Valid first name")
                last_name_update = input('Enter the last name of the contact you would like the last name changed to: ').title()
                if last_name_update.isalpha() == True:
                    print("Valid last name")
                    name_update = first_name_update + " " + last_name_update
                    contacts[email]["Name"] = name_update
                    print(f"The name has been updated. Here is your updated list of contacts: \n{contacts}")
                else: 
                    print("Invalid name entry")
            else: 
                print("Invalid name entry")
        
        elif edit == "3":
            number_update = input('Enter the phone number (separated only by dashes - Example "123-456-7890") you would like the phone number changed to: ')
            verified_phone_number = re.match(r"\d{3}-\d{3}-\d{4}", number_update)
            if verified_phone_number:
                print("Valid phone number") 
                contacts[email]["Phone Number"] = number_update
                print(f"The phone number has been updated. Here is your updated list of contacts: \n{contacts}")
            else:
                print("Invalid phone number entry")
        elif edit == "4":
            category_update = input("""What category would you like this contact to have? Choose a selection by entering a number from the menu below: 
                Category Menu:
                    1 - Friend
                    2 - Family
                    3 - Work
                    """)
            if category_update == "1":
                contacts[email]['Category'] = "Friend"
                print(f"Contact was successfully updated as a friend. Here is your updated list of contacts: \n{contacts}")
            elif category_update == "2":
                contacts[email]['Category'] = "Family"
                print(f"Contact was successfully updated as a family member. Here is your updated list of contacts: \n{contacts}")
            elif category_update == "3":
                contacts[email]['Category']= "Work"
                print(f"Contact was successfully updated as a work colleague. Here is your updated list of contacts: \n{contacts}")
            else:
                print("You entered an invalid choice")
        elif edit == "5": #DO NOT KNOW HOW TO FIX THIS 
            custom_field_category_update = input("What would you like to update the Custom Field Category to for this contact? ").title()
            contacts[email][custom_field_category] = custom_field_category_update
            custom_field_update = input("What would you like to update the custom field to for this contact? ").title()
            contacts[email][custom_field] = custom_field_update
            print(f"Your Custom Field Category and your Custom Field have been updated for this contact to {custom_field_category_update}: {custom_field_update}")
            print(f"Here is your updated list of contacts: \n{contacts}")
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
            
    elif search_choice == "2": # PRINTS IN THE FORMAT THAT I WANT BUT PRINTS ALL THE CONTACTS RATHER THAN JUST THE ONE I AM SEARCHING FOR 
        first_name = input('Enter the first name of the contact you would like to add: ').title()
        if first_name.isalpha() == True:   
            last_name = input('Enter the last name of the contact you would like to add: ').title()
            if last_name.isalpha() == True:
                name = first_name + ' ' + last_name
                if name:
                    for email, name in contacts.items():
                        print("\nEmail:", email)
                        for key in name:
                            print(key + ':', name[key])
                
                else:
                    print("The name you entered does not match any of the contacts")
            else: 
                print("Invalid name entry")
        else:
            print("Invalid name entry")
            
            
    elif search_choice == "3": # PRINTS IN THE FORMAT THAT I WANT BUT PRINTS ALL THE CONTACTS RATHER THAN JUST THE ONE I AM SEARCHING FOR 
        phone_number = input('Enter the phone number (separated only by a dash - Example "123-456-7890")) of the contact you would like to search: ')
        verified_phone_number = re.match(r"\d{3}-\d{3}-\d{4}", phone_number)
        if verified_phone_number:
            for email, phone_number in contacts.items():
                print("\nEmail:", email)
                for key in phone_number:
                    print(key + ':', phone_number[key])
                else:
                    print("The phone number you entered does not match any of the contacts")
    
    else:
        print("You entered an invalid choice")

def display_contacts(contacts):
    sorted_contacts = dict(sorted(contacts.items(), key=lambda item: item[1]['Name']))
    print("Here is a list of your contacts displayed in alphabetical order: ")
    for email, name in sorted_contacts.items():
        print("\nEmail:", email)
        for key in name:
            print(key + ':', name[key])
        
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
            email, first_name, last_name, phone_number = line.strip().split(":")
            my_contacts[email] = {f"{first_name} {last_name} {phone_number}"}
    print(type(my_contacts)) #JUST MAKING SURE IT IS A DICTIONARY 
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