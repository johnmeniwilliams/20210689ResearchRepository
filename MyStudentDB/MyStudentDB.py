# We need to import the os module, which provides a way of using operating system dependent functionality between user and OS.
# This is part of the standard Python utilities library

import os

# define a function to create student record

def create_record():

    # Below "Declares" that the "student_records" variable is a global variable and can be accessed and modified from within the function
    
    global student_records

    # Assigns a value to student_id that is calculated as the length of the student_records dictionary plus 2003

    # Increments student ID by 1 for each record created
    # Prompts the user to enter values for each of the student record fields and assigns them to corresponding variables
    
    student_id = len(student_records) + 2003 
    first_name = input("Enter Student First Name: ")
    last_name = input("Enter Student Last Name: ")
    dob = input("Enter Date of Birth (dd/mm/yyyy): ")
    gender = input("Are you Male or Female: ")
    nationality = input("Enter Nationality: ")
    address = input("Enter Street Address: ")
    suburb = input("Enter Suburb: ")
    city = input("Enter City: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    course_name = input("Enter Course Name (MS Word, MS Excel, MS PowerPoint, MS Access): ")
    student_records[student_id] = {'First Name': first_name, 'Last Name': last_name, 'Date of Birth': dob, 'Gender': gender, 'Nationality': nationality, 'Address': address, 'Suburb': suburb, 'City': city, 'Phone': phone, 'Email': email, 'Course Name': course_name}
    
    # Prints a message to indicate that a new student record has been created, along with the details of the newly added record
    
    print(f"Student Record Created: {student_records[student_id]}")
  
# define a function to display all student records

def display_all_records():
    global student_records
    if not student_records:
        print("No student records found.")
    else:
        for student_id, record in student_records.items():
            print(f"Student ID: {student_id}\nRecord: {record}\n")

# The below will define a function to search and edit student record by searching on user provided student record ID
# User will be asked to specify name of field in record to update
# Example: If the "Course Name" field is selected because the wrong Course was entered you could update it or append to it
# Multiple Course Names need to be seperated with a (,) comma and it is not Letter Case Sensitive

def search_edit_record():
    global student_records
    search_id = int(input("Enter student ID to search: "))
    if search_id not in student_records:
        print("Student record not found.")
    else:
        record = student_records[search_id]
        print(f"Record Found: {record}")
        field = input("Enter field name to edit: ")
        if field not in record:
            print("Invalid field name.")
        else:
            value = input(f"Enter new value for {field}: ")
            record[field] = value
            print(f"Record updated: {record}")

# Now we need to define a function to export all student records to a text file
# Note the below destination text file needs to exist on destination drive example ""E:/Student List Database.txt" and must have prefereed Full NTFS Permissions or minumum Modify Permissions
# Each new Student Course Registration will be appended to next row in the destination Database Text file

def export_records():
    global student_records
    filename = "E:/Student List Database.txt"
    with open(filename, 'w') as file:
        for student_id, record in student_records.items():
            file.write(f"Student ID: {student_id}\nRecord: {record}\n")

# This is the main function to start the program and initialize the Main Menu with numberical options to select from

def main():
    global student_records
    student_records = {}
    while True:
        print("=== MENU ===")
        print("1. Create Student Record")
        print("2. Display all Student Records")
        print("3. Search Student Record to Edit and Save Changes")
        print("4. Export Student Records")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            create_record()
        elif choice == 2:
            display_all_records()
        elif choice == 3:
            search_edit_record()
        elif choice == 4:
            export_records()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
    print("Program terminated.")

if __name__ == '__main__':
    main()
