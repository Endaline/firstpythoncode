# static method = A static method is a method that belongs to the class rather than an instance of the class. 
# It does not require an instance to be called and does not have access to the instance (self) or class (cls) variables. 
# Static methods are defined using the @staticmethod decorator.

class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"Name: {self.name}, Position: {self.position}"    

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Designer"]
        return position in valid_positions
    
employee1 = Employee("Alice", "Manager")
employee2 = Employee("Bob", "Developer")

print(employee1.get_info())
print(employee2.get_info())    
print(Employee.is_valid_position("Manager"))  
print(Employee.is_valid_position("Intern"))  