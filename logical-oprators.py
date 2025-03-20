# Logical oprators = evaluate multiple conditions(or,and not)
#                    or = atleast one condition must be true
#                    and = both conditions must be true
#                    not = inverts the condition (not flase , not true)


#  For or 
temp = 40
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")


# For and

if temp > 36 and is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")


# For not

    
if temp > 36 and not is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")