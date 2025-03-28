# format specifiers = {value:flags} format a valure base on what flag are inserted

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:.2f}") #the 2f is to convert it to 2decimal float value
print(f"Price 2 is ${price2:.1f}") #the 1f is to convert it to 1decimal float value
print(f"Price 3 is ${price3:.3f}") #the 3f is to convert it to 3decimal float value