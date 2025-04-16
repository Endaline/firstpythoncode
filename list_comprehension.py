# List comprhension = A concise way to create lists in python
#                     Compact and easier to resd than traditional loops
#                    [espression for value in iterable if codition]


doubles = []
for x in range (1, 11):
     doubles.append(x * 2)
print(doubles)    

# shorter way

doubles = [x * 2 for x in range (1,11)]
triples = [y * 3 for y in range (1,11)]
sqaures = [z * z for z in range (1,11)]
print(doubles)
print(triples)
print(sqaures)

fruits = ["apple", "orange","banana","coconut"]
fruits = [fruit.upper()for fruit in fruits]
print(fruits)

numbers = [1,-2,3,-4,5,-6,8,-7]
positive_nums = [num for num in numbers if num >=0]
negative_nums = [num for num in numbers if num <=0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print (positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)
