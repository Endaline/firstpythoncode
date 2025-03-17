import math

# to calculte the circumference of a circle 
# formula  C = 2πr 

# radius = float(input("Enter the radius of a circle"))

# circumference = 2 * math.pi * radius

# # to round it to two digit we add 2
# print(f"the circumference is {round(circumference,2)}cm" )  

# To claculate the area of a circle
# formula is πr2

# radius = float(input("Enter the radius of a circle"))

# area=  math.pi * pow(radius,2)

# print(f"the area of a circle is {round(area, 2)}cm^2")

# formula to calculate the hypertunus of a right triangle that is square root of a^2 + b^2
a = float(input("Enter the side A :"))
b = float(input("Enter the side B :"))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"The hypertunus of a right triangle is {round(c,2)} ")