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
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

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

    