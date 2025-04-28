# class methods = A class method is a method that belongs to the class rather than an instance of the class.
# It takes the class as its first argument (usually named cls) and can access class variables and methods.
# Class methods are defined using the @classmethod decorator.

class Student:
    
    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"Name: {self.name}, GPA: {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"
    
student1 = Student("Alice", 3.2)
student2 = Student("Bob", 2.0)
student3 = Student("Charlie", 4.0)
print(student1.get_info())
print(student2.get_info())    

print(Student.get_count())   
print(Student.get_average_gpa())   
    