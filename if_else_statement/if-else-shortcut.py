# A conditional expression = A one -line shortcut for the if-else statement (ternary operator)
                            #  Print or assign one of  two values based on condition 
                        #     X if condition else Y


num = 9
a = 6
b = 7
age = 25

result = "Even" if num % 2 == 0 else "Odd"
print(result)

max_num = a if a > b else b
min_num = a if a < b else b

status = "Adult" if age > 18 else "Tenager"


print (max_num)
print (min_num)
print(status)

baby_age = 0

while baby_age < 18: 
    print ("Not an adult yet")
    baby_age = baby_age + 1



# How to define a function in Python
def funtion(a,b,c):
    result = a + b + c
    return result

sum = funtion(6,8,4)
print (sum)