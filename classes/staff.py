from classes.person import Person
import csv

class Staff(Person):

    all_staff_list = []

    @classmethod
    def all_staff(cls, file_path):

        with open(file_path, mode='r', newline='') as csvfile:

            staff_data_reader = csv.DictReader(csvfile)
            for staff_data in staff_data_reader:
                a_staff = Staff(**staff_data)
                cls.all_staff_list.append(a_staff)
        return cls.all_staff_list

    def __init__(self,name=None,age=None,role=None,employee_id=None,password=None):
        super().__init__(name,age,role)
        self.employee_id = int(employee_id)
        self.password = password

    def __repr__(self):
        return f"Name: {self.name} | Age: {self.age} | Role: {self.role}"
    
    
