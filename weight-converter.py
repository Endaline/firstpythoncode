# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("kilogram or pounds? (K or L)")

if unit == "K":
  weight = weight * 2.205  # Convert kg to lbs
#   print(f"Your weight is {round(weight,2)} {unit}")

elif unit == "L":
  weight = weight / 2.205  # Convert lbs to kg
  unit = "kgs." 
#   print(f"Your weight is {round(weight,2)} {unit}")


else:
  print(f"{unit} is not a valid unit")
#   either you add exit or you add the print under each of them
exit()  # Stop execution if input is invalid

print(f"Your weight is {round(weight,2)} {unit}")






