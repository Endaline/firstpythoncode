# super() function = It is used to call a method from the parent class. It allows you to extend the functionality of the inherited methods .

class Parent():
    def __init__(self,fname,age):
        self.name = fname
        self.age = age
    def show(self):    
        print(f"Parent class: {self.name} is {self.age} years old")

class Child(Parent):
    def __init__(self,fname,age):
        super().__init__(fname,age)
    
c = Child("Mimi",23)    
c.show()