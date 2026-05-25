# Creating a Validator class to validate all submitted information
class Validator:

    # Creating method to validate whether a value is not empty
    def validateRequired(self, value):
        return value.strip() != ""

    # Creating method to validate student ID
    def validateStudentID(self, student_id):
        return student_id.isdigit() and len(student_id) <= 7

    # Creating method to validate instructor ID
    def validateInstructorID(self, instructor_id):
        return instructor_id.isdigit() and len(instructor_id) <= 5

    # Creating method to validate name
    def validateName(self, name):
        invalid_characters = "!\"@#$%^&*()_=+,<>/?;:[]{}\\"

        if not self.validateRequired(name):
            return False

        for character in name:
            if character in invalid_characters:
                return False

        return True

    # Creating method to validate email address
    def validateEmail(self, email):
        invalid_characters = "!\"'#$%^&*()=+,<>/?;:[]{}\\"

        if not self.validateRequired(email):
            return False

        for character in email:
            if character in invalid_characters:
                return False

        return True


# Creating a parent class to store shared information
class Person:

    # Creating constructor for shared person information
    def __init__(self, passed_name, passed_email):
        self.name = passed_name
        self.email = passed_email

    # Creating method to display shared information
    def displayInformation(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")


# Creating Student class using inheritance from Person
class Student(Person):

    # Creating constructor for student information
    def __init__(self, passed_name, passed_email, passed_student_id, passed_program):
        super().__init__(passed_name, passed_email)
        self.student_id = passed_student_id
        self.program_of_study = passed_program

    # Creating augmented method to display student information
    def displayInformation(self):
        print("\nStudent Record")
        super().displayInformation()
        print(f"Student ID: {self.student_id}")
        print(f"Program of Study: {self.program_of_study}")


# Creating Instructor class using inheritance from Person
class Instructor(Person):

    # Creating constructor for instructor information
    def __init__(self, passed_name, passed_email, passed_instructor_id, passed_institution, passed_degree):
        super().__init__(passed_name, passed_email)
        self.instructor_id = passed_instructor_id
        self.last_institution = passed_institution
        self.highest_degree = passed_degree

    # Creating augmented method to display instructor information
    def displayInformation(self):
        print("\nInstructor Record")
        super().displayInformation()
        print(f"Instructor ID: {self.instructor_id}")
        print(f"Last Institution Graduated From: {self.last_institution}")
        print(f"Highest Degree Earned: {self.highest_degree}")


# Creating function to get validated individual type
def getIndividualType():
    while True:
        individual_type = input("Enter individual type, instructor or student: ").lower()

        if individual_type == "student" or individual_type == "instructor":
            return individual_type

        print("Invalid type. Please enter instructor or student.")


# Creating function to get validated name
def getName(validator):
    while True:
        name = input("Enter individual name: ")

        if validator.validateName(name):
            return name

        print("Invalid name. Please remove invalid characters.")


# Creating function to get validated email
def getEmail(validator):
    while True:
        email = input("Enter email address: ")

        if validator.validateEmail(email):
            return email

        print("Invalid email. Please remove invalid characters.")


# Creating function to get validated student ID
def getStudentID(validator):
    while True:
        student_id = input("Enter student ID: ")

        if validator.validateStudentID(student_id):
            return student_id

        print("Invalid student ID. Please enter a number that is 7 or less digits long.")


# Creating function to get validated program of study
def getProgramOfStudy(validator):
    while True:
        program = input("Enter program of study: ")

        if validator.validateRequired(program):
            return program

        print("Program of study is required.")


# Creating function to get validated instructor ID
def getInstructorID(validator):
    while True:
        instructor_id = input("Enter instructor ID: ")

        if validator.validateInstructorID(instructor_id):
            return instructor_id

        print("Invalid instructor ID. Please enter a number that is 5 or less digits long.")


# Creating function to get validated last institution
def getLastInstitution(validator):
    while True:
        institution = input("Enter last institution graduated from: ")

        if validator.validateRequired(institution):
            return institution

        print("Last institution graduated from is required.")


# Creating function to get validated highest degree
def getHighestDegree(validator):
    while True:
        degree = input("Enter highest degree earned: ")

        if validator.validateRequired(degree):
            return degree

        print("Highest degree earned is required.")


# Creating function to ask user if they want to continue
def askToContinue():
    while True:
        answer = input("Would you like to enter another individual? yes/no: ").lower()

        if answer == "yes" or answer == "y":
            return True

        elif answer == "no" or answer == "n":
            return False

        print("Invalid response. Please enter yes or no.")


# Creating function to gather one college record
def getCollegeRecord(validator):
    individual_type = getIndividualType()
    name = getName(validator)
    email = getEmail(validator)

    if individual_type == "student":
        student_id = getStudentID(validator)
        program = getProgramOfStudy(validator)

        return Student(name, email, student_id, program)

    instructor_id = getInstructorID(validator)
    institution = getLastInstitution(validator)
    degree = getHighestDegree(validator)

    return Instructor(name, email, instructor_id, institution, degree)


# Creating main program logic
def main():
    validator = Validator()
    college_records = []

    while True:
        record = getCollegeRecord(validator)
        college_records.append(record)

        if not askToContinue():
            break

    print("\nAll College Records:")

    for number, record in enumerate(college_records, start=1):
        print(f"\nRecord {number}")
        record.displayInformation()


# Creating program start point
main()