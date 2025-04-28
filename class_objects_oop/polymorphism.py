# Polymorphism = Greek word that means "many shapes"
# Polymorphism allows us to define methods in the child class with the same name as defined in the parent class

# Two ways to achieve polymorphism
# 1. Inheritance = An object could be treated as the same type as its parent class
# 2. Duck typing = Object must have necessary methods/attributes and properties to be considered as a certain type
from abc import ABC, abstractmethod
# Example of polymorphism using inheritance
class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **2

class Square(Shape):
 def __init__(self,side):
        self.side = side

 def area(self):
        return self.side **2       

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height  
     
# adding a class that has nothing to do with shapes
class Pizza(Circle):
    def __init__(self,topping,radius):
        self.topping = topping
        # since we already have a radius in the Circle class, we can use super() to call the __init__ method of the Circle class
        super().__init__(radius)
shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()}cm")


# Example of polymorphism using duck typing    
# If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
    
    # adding a class that has nothing to do with animals
class Car:
    alive = True
    def speak(self):
        # let's rename our honk method to speak
        # so that it can be used in the same way as the speak method in the Dog and Cat classes
        # this is a method that is not related to the Animal class
        print("Honk!")    

animals = [Dog(), Cat(), Car()]   
for animal in animals:
    print(animal.speak())    
    print(animal.alive) # this will print True for all the classes   