# nested loop = A loop inside another loop(outer, inner)

# for x in range(4):
#     for y in range(1,10):
#         print(y, end=" ")
#     print(x)
    
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print(x)