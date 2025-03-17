# if  = Do some code only If some condition is True
# Else do something else

# about operator
operator = input("Enter an opratore (+,-,*,/)")
num1 = float(input("Enter num1"))
num2 = float(input("Enter num2"))

if operator == "+":
    result = num1 + num2
    print(round(result,2))
elif operator == "*":
    result = num1 * num2
    print(round(result,2))
elif operator == "-":
    result = num1 - num2
    print(round(result,2))
elif operator == "/":
    result = num1 - num2
    print(round(result,2))
elif operator == "%":
    result = num1 % num2
    print(round(result,2))
else:
    print(f"{operator} is not valid")


# about name
name = input("What is your name?")
if name == "":
    print("You did not type in your name")
else:
    print(f"My name is {name}")


    # about age
age = int(input("Enter your age :"))

if age >=25:
    print("The decision is left for you to make you are a full grown adult  ")
elif age >= 18:
    print("Yoo You are old enough to take alcohol")

elif age <= 17:
    print("You are underage you can't take alcohol ")
else:
    print("Do whatever you like you are an adult")


