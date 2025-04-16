# Membership operators = used to test whether a value or variable is found in a sequence (string,list, tuple, set or dictionary)
#                      1.in
#                      2.not in

# email = "Brocode@gmail.com"

# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalide email")    

students = {"Miriam","Chioma","Endy"}   

student = input ("Enter the name of a student: ")

if student not in students:
     print(f"{student} is not a student")    
else:
    print(f"{student} is a student")

   