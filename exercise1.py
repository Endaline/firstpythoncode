# Exercise 1


# Calculate Area of a Rectangle which is A = lw

# lets convert it to a float
length = float(input("Enter the length"))
wight = float(input("Enter the wight"))

area = length * wight

print (f"The area is {area}cm2")



# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?")
price = float(input("What is the price of the item?"))

qunatity = int(input("How amny quantity are you buying?"))

total = price * qunatity

print("this is the total price of your item", total)