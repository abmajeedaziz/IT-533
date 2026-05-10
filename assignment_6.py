# Creating an empty list to store employee information
employees = []

# Keep asking for employee information
while True:

    #  Employee ID Validation 
    while True:
        employee_id = input("Enter Employee ID: ")

        if employee_id.isdigit() and len(employee_id) <= 7:
            break
        else:
            print("Invalid Employee ID. Must be numeric and 7 digits or less.")

    #  Employee Name Validation 
    while True:
        employee_name = input("Enter Employee Name: ")

        valid_name = True

        for character in employee_name:
            if not (character.isalpha() or character == " " or character == "'" or character == "-"):
                valid_name = False

        if employee_name != "" and valid_name:
            break
        else:
            print("Invalid name. Enter again !!!")

    #  Employee Email Validation 
    invalid_email_characters = "!\"'#$%^&*()=+,<>/?;:[]{}\\"

    while True:
        employee_email = input("Enter Employee Email Address: ")

        valid_email = True

        for character in employee_email:
            if character in invalid_email_characters:
                valid_email = False

        if employee_email != "" and valid_email:
            break
        else:
            print("Invalid email address. Enter again !!!")

    #  Employee Address Validation 
    invalid_address_characters = "!\"'@$%^&*_=+<>?;:[]{}"

    while True:
        employee_address = input("Enter Employee Address (optional): ")

        if employee_address == "":
            break

        valid_address = True

        for character in employee_address:
            if character in invalid_address_characters:
                valid_address = False

        if valid_address:
            break
        else:
            print("Invalid address. Enter again !!!")

    #  Employee Salary Validation 
    while True:
        try:
            employee_salary = float(input("Enter Employee Salary: "))

            if 18 <= employee_salary <= 27:
                break
            else:
                print("Salary must be between 18 and 27.")

        except ValueError:
            print("Invalid salary. Enter again !!!")

    #  Store Employee Information 
    employee = {
        "Employee ID": employee_id,
        "Employee Name": employee_name,
        "Employee Email": employee_email,
        "Employee Address": employee_address,
        "Employee Salary": employee_salary
    }

    employees.append(employee)

    #  Asking User to Continue 
    continue_choice = input("Do you want to add another employee? yes/no: ").lower()

    if continue_choice != "yes":
        break


#  Updating Information Using Comprehensions 
updated_employees = [
    {
        "Employee ID": employee["Employee ID"],
        "Employee Name": employee["Employee Name"] + " IT Department",
        "Employee Email": employee["Employee Email"],
        "Employee Address": employee["Employee Address"],
        "Employee Salary": employee["Employee Salary"] * 1.30
    }

    for employee in employees
]


#  Printing Updated Employee Information 
print("\nUpdated Employee Information:")
print(updated_employees)