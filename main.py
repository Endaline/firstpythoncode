# Typescasting: This is the process of converting a variable from one data type to another
#  str(), int(), float(), bool()

name = "Jone Deo"
age = 24
gpa = 4.0
is_student = True

# to get the type of data type
print(type(is_student)) 

# how to convert float() to int()
gpa = int(gpa) 
print(gpa)

# how to convert int() to float()
age = float(age)
print(age)

# how to convert int() to str() though the iput is showing as an int() but the type is a str()
age = str(age)
age += "1"
print(age)


# Input() = A function that prompts the user to enter data
# Returns the entered data as a string

name = input("What is your name?")
# we can also convert the input() to int 
age = int(input("How old are you?"))
# the input is accepting the age as str() so we convert it to int()
# age = int(age)
age += 1

print(f"Hello {name}")
print("Happy birthday")
print(f"You are {age} years old")