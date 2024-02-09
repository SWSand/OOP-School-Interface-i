import csv
from classes.school import School 
from classes.student import Student
from classes.staff import Staff

school = School('Ridgemont High') 

# print(school.name)
# print(school.staff)
# print(school.students)

# bob = Student("bob","4", "Student", "23345", "xyz123")
# print(bob)

# alice = Staff("alice","4","Teahcer","1234","pwd123")
# print(alice)

Student.all_students("./data/students.csv")

# with open("./data/students.csv", mode='r', newline='') as csvfile:

#     student_data_reader = csv.DictReader(csvfile)
#     for student_data in student_data_reader:
#         # print(student_data)
#         a_student = Student(**student_data)
#         print(a_student)

Staff.all_staff("./data/staff.csv")

# with open("./data/staff.csv", mode='r', newline='') as csvfile:

#     staff_data_reader = csv.DictReader(csvfile)
#     for staff_data in staff_data_reader:
#         # print(staff_data)
#         a_staff = Staff(**staff_data)
#         print(a_staff)

main_menu_message = '''
--------------------------------
Welcome, Richard. Your access level is Principal
    What would you like to do?
    Options:
    1 List All Students
    2 View Individual Student <student_id>
    3 Add a Student
    4 Remove a Student <student_id>
    5 Quit
'''

def display_main_menu():

    user_main_menu_input = input(main_menu_message)
    print(user_main_menu_input)

    if user_main_menu_input == "1":
        display_all_students_menu()
        display_main_menu()
    elif user_main_menu_input == "2":
        display_view_invdividual_student_menu()
        display_main_menu()
    elif user_main_menu_input == "3":
        display_add_a_student_menu()
        display_main_menu()
    elif user_main_menu_input == "4":
        display_remove_a_student_menu()
        display_main_menu()
    elif user_main_menu_input == "5":
        exit()
    else:
        print("Invalid input, please type 1,2,3,4,or 5")
        display_main_menu()



def display_all_students_menu():
    print("Display all students")

def display_view_invdividual_student_menu():
    student_name = input("What is the name of the student you want to view?")
    pass

def display_add_a_student_menu():
    print("Add Student")
    pass

def display_remove_a_student_menu():
    print("Remove Student")
    pass

display_main_menu()
