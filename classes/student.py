import csv
from classes.person import Person

class Student(Person):
    all_students_list = []

    @classmethod
    def all_students(cls,file_path):

        with open(file_path, mode='r', newline='') as csvfile:

            student_data_reader = csv.DictReader(csvfile)
            for student_data in student_data_reader:
                a_student = Student(**student_data)
                cls.all_students_list.append(a_student)
                # print(a_student)
        return cls.all_students_list

    def __init__(self,name=None,age=None,role=None,school_id=None,password=None):
        super().__init__(name,age,role)
        self.school_id = school_id
        self.password = password

    def __repr__(self):
        return f"Name: {self.name} | Age: {self.age} | Role: {self.role} | School ID: {self.school_id} | Password: {self.password}"




# alice = Student('alice', '4', "Student", "23345","xyz123")

# print(alice)