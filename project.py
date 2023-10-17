# Define a dictionary to store student data
students = {}

# Define a list of units
units = ["Networking", "C programming", "Data Structures and Algorithm", "Economics", "Marketing"]

# Define a function to input student data
def input_student_data():
    for i in range(5):
        name = input("Enter name of student {}: ".format(i+1))
        reg_no = input("Enter registration number of student {}: ".format(i+1))
        grades = []
        for unit in units:
            grade = int(input("Enter grade for {} for student {}: ".format(unit, i+1)))
            grades.append(grade)
        students[reg_no] = {"name": name, "grades": grades}

# Define a function to calculate average grade
def calculate_average_grade(reg_no):
    grades = students[reg_no]["grades"]
    return sum(grades) / len(grades)

# Define a function to find highest and lowest grade
def find_highest_and_lowest_grade():
    highest_grade = 0
    lowest_grade = 100
    highest_reg_no = ""
    lowest_reg_no = ""
    for reg_no in students:
        average_grade = calculate_average_grade(reg_no)
        if average_grade > highest_grade:
            highest_grade = average_grade
            highest_reg_no = reg_no
        if average_grade < lowest_grade:
            lowest_grade = average_grade
            lowest_reg_no = reg_no
    print("Highest grade is {} by student {} with registration number {}".format(highest_grade, students[highest_reg_no]["name"], highest_reg_no))
    print("Lowest grade is {} by student {} with registration number {}".format(lowest_grade, students[lowest_reg_no]["name"], lowest_reg_no))

# Define a function to search for student grade by registration number
def search_student_grade():
    reg_no = input("Enter registration number of student: ")
    if reg_no in students:
        print("Average grade for student {} with registration number {} is {}".format(students[reg_no]["name"], reg_no, calculate_average_grade(reg_no)))
    else:
        print("Student with registration number {} not found".format(reg_no))

# Call the functions to input data, calculate average grade, find highest and lowest grade, and search for student grade
input_student_data()
for reg_no in students:
    print("Average grade for student {} with registration number {} is {}".format(students[reg_no]["name"], reg_no, calculate_average_grade(reg_no)))
find_highest_and_lowest_grade()
search_student_grade()