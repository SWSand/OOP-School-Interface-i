class Person:

    # *Instance Attributes:
    #  -name
    #  -age (int)
    #  -role
    
    def __init__(self,name,age,role):
        self.name = name
        self.age = int(age) # TODO: Validation handle cast error if age is invalid
        self.role = role
    
    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | Role: {self.role}"

    def __repr__(self):
        return f"{self.name} {self.age} {self.role}"

# alice = Person("Alice", "5", "student")
# bob = Person("Bob", 6, "student")

# print(alice)
# print(bob)
# print([alice,bob])