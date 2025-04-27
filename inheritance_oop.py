# inheritance = inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class = base class
# Child class = derived class
# The child class will have all the attributes and methods of the parent class, and it can also have its own attributes and methods.
# Types of inheritance
# 1. Single inheritance
# 2. Multiple inheritance
# 3. Multilevel inheritance
# 4. Hierarchical inheritance
# 5. Hybrid inheritance

# Example of single inheritance
class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def run(self):
        print(f"{self.name} is running")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} says Squeak!")

dog = Dog("Bubby")
cat = Cat("Mimi")
mouse = Mouse("Micky")

dog.eat()
cat.sleep()
mouse.run()
dog.sleep()
cat.eat()
mouse.run()
dog.run()
dog.sleep()
cat.run()
dog.speak()
cat.speak()
mouse.speak()

# Mltiple inheritance = This is when a when a child inherits from more than one parent class. The child class will have all the attributes and methods of the parent classes.
# Example of multiple inheritance
class Father:
    def skills(self):
        print("Father: Gardening, Carpentry")

class Mother:
    def skills(self):
        print("Mother: Cooking, Painting")

# Child inherits from both Father and Mother
class Child(Father, Mother):
    def skills(self):
        # Call skills from both parents
        Father.skills(self)
        Mother.skills(self)
        print("Child: Programming, Dancing")

# Create object
c = Child()
c.skills()

# multilevel inheritance = This is when a  class is derived from another derived class. There exists multiple layers of inheritance. We can imagine it as a grandparent-parent-child relationship..
# Example of multilevel inheritance
class Animal:
    # grandparent class
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name}  is sleeping")
class Pray(Animal):
    def flee(self):
        print(f"{self.name}  is fleeing")
class Predator(Animal):
    def hunt(self):
        print(f"{self.name}  is hunting")

class Rabbit(Pray):
    pass

class Lion(Predator):
    pass

class Fish(Pray, Predator):
    pass

rabbit = Rabbit("Bugs")
lion = Lion("Tom")
fish = Fish("Nemo")    

rabbit.flee()
lion.hunt()
fish.hunt()
fish.flee()
fish.eat()
fish.sleep()

# hierarchical inheritance = Hierarchical inheritance occurs when multiple child classes inherit from a single parent class.
# Example of hierarchical inheritance

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")

class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")

class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching.")

s1 = Student("Alice")
t1 = Teacher("Mr. John")

s1.introduce()
s1.study()

t1.introduce()
t1.teach()

# hybrid inheritance = Hybrid inheritance is a combination of two or more types of inheritance. It can be a combination of single, multiple, multilevel, or hierarchical inheritance.
# Example of hybrid inheritance

# parent class
class CEO: 
   def ceoMethod(self):
      print ("I am the CEO")
      
class Manager(CEO): 
   def managerMethod(self):
      print ("I am the Manager")

class Employee1(Manager): 
   def employee1Method(self):
      print ("I am Employee one")
      
class Employee2(Manager, CEO): 
   def employee2Method(self):
      print ("I am Employee two")      

# creating instances 
emp1= Employee1()
emp1.employee1Method()

emp2 = Employee2()
# method calls
emp2.managerMethod() 
emp2.ceoMethod()
emp2.employee2Method()