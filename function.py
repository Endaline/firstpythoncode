# function = A block of code that performs a specific task
# return = A statement that ends the function and sends a value back to the caller
def birthday():
    print("Happy Birthday to you!")

birthday()
birthday()
birthday()  

def add(a,b):
     c = a + b
     return c
def subtract(a,b):
     c = a - b
     return c           
def multiply(a,b):
     c = a * b
     return c
def divide(a,b):
     c = a / b
     return c

print(add(26,16))
print(subtract(26,16))
print(multiply(26,16))
print(divide(26,16 ))


def create_name(first, last):
     first = first.capitalize()
     last = last.capitalize()
     return  first + " " + last

full_name = create_name("john", "doe")
print(full_name)
