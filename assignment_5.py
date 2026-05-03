# Creating a single list that contains the original exported employee data
employee_data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]

# Creating empty lists for the required assignment output
employee_records = []
underpaid_salaries = []
company_raises = []

# Creating temporary variables to collect employee information
employee_id = None
employee_name = None
hourly_wage = None

# Creating logic to sort the mixed data into database-like dictionaries
for item in employee_data:

    # Creating check for employee ID numbers
    if type(item) == int:
        employee_id = item

    # Creating check for employee names
    elif type(item) == str:
        employee_name = item

    # Creating check for hourly wage values
    elif type(item) == float:
        hourly_wage = item

    # Creating condition to ignore boolean values
    elif type(item) == bool:
        continue

    # Creating dictionary when all employee data parts are available
    if employee_id is not None and employee_name is not None and hourly_wage is not None:

        employee = {
            "employee_id": employee_id,
            "employee_name": employee_name,
            "hourly_wage": hourly_wage
        }

        # Creating condition to prevent duplicate employee records
        if employee not in employee_records:
            employee_records.append(employee)

        # Creating reset of temporary variables for next employee
        employee_id = None
        employee_name = None
        hourly_wage = None

# Creating total_hourly_rate for each employee
for employee in employee_records:
    employee["total_hourly_rate"] = round(employee["hourly_wage"] * 1.3, 2)

# Creating logic to find underpaid salaries
for employee in employee_records:
    if 28.15 <= employee["total_hourly_rate"] <= 30.65:
        underpaid_salaries.append(employee)

# Creating logic to calculate employee raises
for employee in employee_records:

    hourly_wage = employee["hourly_wage"]

    # Creating 5% raise condition
    if 22 <= hourly_wage <= 24:
        raise_amount = hourly_wage * 0.05

    # Creating 4% raise condition
    elif 24 < hourly_wage <= 26:
        raise_amount = hourly_wage * 0.04

    # Creating 3% raise condition
    elif 26 < hourly_wage <= 28:
        raise_amount = hourly_wage * 0.03

    # Creating standard 2% raise condition
    else:
        raise_amount = hourly_wage * 0.02

    raise_record = {
        "employee_name": employee["employee_name"],
        "raise_amount": round(raise_amount, 2)
    }

    company_raises.append(raise_record)

# Creating print output for employee records
print("Employee Records:")
for employee in employee_records:
    print(employee)

# Creating print output for underpaid salaries
print("\nUnderpaid Salaries:")
for employee in underpaid_salaries:
    print(employee)

# Creating print output for company raises
print("\nCompany Raises:")
for employee in company_raises:
    print(employee)