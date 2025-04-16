# Tuple() is a collection which is ordered and unchangeable. Allows duplicate members.

fruits = ("apple", "banana", "cherry","orange","kiwi","melon","mango")
y = list(fruits) # to convert tuple to list
# y.append("pear") # to add an item
# y.remove("banana") # to remove an item
# y.pop() # to remove the last item
# y.clear() # to clear the list
# y.sort() # to sort the list alphapetically
# y.reverse() # to reverse the list
fruits = tuple(y) # to convert list to tuple

i = 0
while i < len(fruits): 
    print(fruits[i])
    i = i + 1