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


# with open("./data/staff.csv", mode='r', newline='') as csvfile:

#     staff_data_reader = csv.DictReader(csvfile)
#     for staff_data in staff_data_reader:
#         # print(staff_data)
#         a_staff = Staff(**staff_data)
#         print(a_staff)