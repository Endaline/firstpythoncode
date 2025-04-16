# # Dictionary items are ordered, changeable, and do not allow duplicates.

# car ={"brand":"Ford","model":"Mustang","year":1964, "name":"Endaline"}

# # How to add a new key-value pair to a dictionary
# car["color"] ="red"
# print(car)

# # The keys() method will return a list of all the keys in the dictionary.

# x = car.keys()
# print(x)

# # The values() method will return a list of all the values in the dictionary.
# # x = car.values()
# # print(x)

# car ["provision"] = "goldenmorn"
# x = car.values()
# print(x)


# how to loop through a nested dictionary
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
 
# for x,obj in myfamily.items():
#     print(x)

#     for y in obj:
#         print(y + ":", obj[y])

capitals ={"USA": "Washington D.C","india":"New Delhi","China":"Beijing","Russia":"Moscow"}     

# print(capitals.get("USA")) 
# capitals.update({"Germany":"Berlin"}) to add to the existing list
# capitals.pop("China") to remove from the existing list
# capitals.popitem() to remove the last item
# capitals.clear() to remove everything
# key = capitals.keys() to get all the keys
# value = capitals.values() to get all the value
# items = capitals.items() items returns tuple inside a list
for key,value in capitals.items():
    print(f"{key} : {value}")
