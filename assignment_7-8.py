
# Importing json so employee data can be written to a JSON file
import json


# Creating a function to validate employee ID
def validate_employee_id(employee_id):
    return employee_id.isdigit() and len(employee_id) <= 7


# Creating a function to validate employee name
def validate_employee_name(employee_name):
    allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '-"

    if employee_name.strip() == "":
        return False

    for character in employee_name:
        if character not in allowed_characters:
            return False

    return True


# Creating a function to validate employee email address
def validate_employee_email(employee_email):
    invalid_characters = "!\"'#$%^&*()=+,<>/?;:[]{}\\"

    if employee_email.strip() == "":
        return False

    for character in employee_email:
        if character in invalid_characters:
            return False

    return True


# Creating a function to validate employee address
def validate_employee_address(employee_address):
    invalid_characters = "!\"'@$%^&*_=+<>?;:[]{}"

    if employee_address.strip() == "":
        return True

    for character in employee_address:
        if character in invalid_characters:
            return False

    return True


# Creating a function to validate employee salary
def validate_employee_salary(employee_salary):
    try:
        employee_salary = float(employee_salary)

        if 18 <= employee_salary <= 27:
            return True

        return False

    except ValueError:
        return False


# Creating a function to gather and validate employee ID
def get_employee_id():
    while True:
        employee_id = input("Enter employee ID: ")

        if validate_employee_id(employee_id):
            return int(employee_id)

        print("Invalid employee ID. Please enter a number that is 7 or less digits long.")


# Creating a function to gather and validate employee name
def get_employee_name():
    while True:
        employee_name = input("Enter employee name: ")

        if validate_employee_name(employee_name):
            return employee_name

        print("Invalid employee name. Please use letters, spaces, apostrophes, or hyphens only.")


# Creating a function to gather and validate employee email
def get_employee_email():
    while True:
        employee_email = input("Enter employee email address: ")

        if validate_employee_email(employee_email):
            return employee_email

        print("Invalid employee email. Please remove invalid special characters.")


# Creating a function to gather and validate employee address
def get_employee_address():
    while True:
        employee_address = input("Enter employee address, or press Enter to skip: ")

        if validate_employee_address(employee_address):
            return employee_address

        print("Invalid employee address. Please remove invalid special characters.")


# Creating a function to gather and validate employee salary
def get_employee_salary():
    while True:
        employee_salary = input("Enter employee salary between 18 and 27: ")

        if validate_employee_salary(employee_salary):
            return float(employee_salary)

        print("Invalid employee salary. Please enter a decimal number between 18 and 27.")


# Creating a function to gather one employee record
def get_employee_record():
    employee = {
        "employee_id": get_employee_id(),
        "employee_name": get_employee_name(),
        "employee_email": get_employee_email(),
        "employee_address": get_employee_address(),
        "employee_salary": get_employee_salary()
    }

    return employee


# Creating a function to ask if the user wants to enter another employee
def ask_to_continue():
    while True:
        answer = input("Would you like to enter another employee? yes/no: ").lower()

        if answer == "yes" or answer == "y":
            return True

        elif answer == "no" or answer == "n":
            return False

        print("Invalid response. Please enter yes or no.")


# Creating a function to gather all employee information
def gather_employee_data():
    employees = []

    while True:
        employee = get_employee_record()
        employees.append(employee)

        if not ask_to_continue():
            break

    return employees


# Creating a function that uses comprehension to add IT Department to each employee name
def add_department_to_names(employees):
    return [
        {
            **employee,
            "employee_name": employee["employee_name"] + " IT Department"
        }
        for employee in employees
    ]


# Creating a function that uses comprehension to increase salary by 30%
def increase_salary_with_benefits(employees):
    return [
        {
            **employee,
            "employee_salary": round(employee["employee_salary"] * 1.3, 2)
        }
        for employee in employees
    ]


# Creating a function to write the final employee list to a JSON file
def write_employees_to_json(employees):
    with open("employee_data.json", "w") as file:
        json.dump(employees, file, indent=4)


# Creating a function to print the final employee list
def print_employee_data(employees):
    print("\nFinal Updated Employee Information:")

    for number, employee in enumerate(employees, start=1):
        print(f"{number}. {employee}")


# Creating main program logic
def main():
    employees = gather_employee_data()

    employees = add_department_to_names(employees)

    employees = increase_salary_with_benefits(employees)

    write_employees_to_json(employees)

    print_employee_data(employees)


# Creating the program start point
main()