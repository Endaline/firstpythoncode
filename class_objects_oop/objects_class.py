# Object = Object is a bundle of related attributes(variables) and methods(functions)
# Class = Class is a blueprint for creating objects,it is a collection of objects

# Example of class and object

class Car:
    def __init__(self,color,name):
# Note: The __init__() function is called automatically every time the class is being used to create a new object.  
# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:      
        self.color = color
        self.name = name

car1 = Car("black","Lambor")        
        
print(car1.name)
print(car1.color)

class Student:
    class_year = 2024
    num_student = 0
    def __init__(self,name,age):
        self.name = name
        self.age =age
        Student.num_student += 1

student1 = Student("Endy","24")  
student2 = Student("Mimi","23")     
student3 = Student("Chioma","27")     

print(student1.name) 
print(student1.age) 
print(student2.name) 
print(student2.age) 
print(student3.name) 
print(student3.age) 
print(Student.class_year) 
print(Student.num_student)