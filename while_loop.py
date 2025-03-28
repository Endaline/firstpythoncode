#While loop excute some codes while some conditions remain true

# food = input("Enter a food you like:(q to quit) ")

# while not food == "q": # while food is not equal to q don't say bye
#     print(f"You like {food}")
#     food = input("Enter another food you like:(q to quit) ")

# print ("bye")

num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num >10 :
    print(f"the {num} is invalid")
    num = int(input("Enter a number between 1 and 10"))
print(f"Your number is {num}")
