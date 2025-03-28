# name = input("Enter your username: ")
# phone_number = input("Enter your phone number:# ")
# result =len(name)  # len() is a built-in function that returns the length of an object
# if result > 10:
#     print("Your name is too long")
# else:
#     print("Your name is short")
# result = name.find("I")  # find() is a built-in function that returns the index of the first occurrence of a substring in a string
# result =name.rfind("e")  # rfind() is a built-in function that returns the index of the last occurrence of a substring in a string

# it will return -1 if it does not find the substring

# result = name.index("I")  # index() is a built-in function that returns the index of the first occurrence of a substring in a string
# result = name.rindex("I")  # rindex() is a built-in function that returns the index of the last occurrence of a substring in a string
# result = name.upper()  # upper() is a built-in function that returns a new string with all characters in uppercase
# result = name.lower()  # lower() is a built-in function that returns a new string with all characters in lowercase
# result = name.capitalize()  # capitalize() is a built-in function that returns a new string with the first character in uppercase
# result = name.title()  # title() is a built-in function that returns a new string with the first character of each word in uppercase
# result = name.strip()  # strip() is a built-in function that returns a new string with leading and trailing whitespace removed
# result = name.lstrip()  # lstrip() is a built-in function that returns a new string with leading whitespace removed
# result = name.rstrip()  # rstrip() is a built-in function that returns a new string with trailing whitespace removed
# result = name.split()  # split() is a built-in function that returns a list of substrings separated by whitespace
# result = name.split("I")  # split() is a built-in function that returns a list of substrings separated by a specified character
# result = name.join("I")  # join() is a built-in function that returns a new string with a specified character inserted between each character of a string
# result = name.startswith("I")  # startswith() is a built-in function that returns True if a string starts with a specified substring
# result = name.endswith("I")  # endswith() is a built-in function that returns True if a string ends with a specified substring
# result = name.isalpha()  # isalpha() is a built-in function that returns True if a string contains only alphabetic characters
#  isalpha()  returns false if there is a space or a number
# result = name.isdigit()  # isdigit() is a built-in function that returns True if a string contains only numeric characters
# result = name.isalnum()  # isalnum() is a built-in function that returns True if a string contains only alphanumeric characters
# result = name.islower()  # islower() is a built-in function that returns True if a string contains only lowercase characters
# result = name.isupper()  # isupper() is a built-in function that returns True if a string contains only uppercase characters
# result = name.istitle()  # istitle() is a built-in function that returns True if a string is in title case
# result = name.isspace()  # isspace() is a built-in function that returns True if a string contains only whitespace characters
# result = name.isprintable()  # isprintable() is a built-in function that returns True if a string is printable



# result = phone_number.replace("1", "6")  # replace() is a built-in function that returns a new string with all occurrences of a substring replaced by another substring
# result = phone_number.count("1") # count() is a built-in function that returns the number of occurrences of a substring in a string



# validation of user input
# 1 the username is not more than 12 characters
# 2 the username must not contain spaces
# 3 username must not contain digits
username = input("Enter your username: ")
if len(username) > 12:
    print("Username can't be more than 12 characters")
# elif " " in username:
    # or use 
elif not username.find("") == -1:    
    print("Username must not contain spaces")
elif username.isdigit():
    print("Username must not contain digits")
else:
    print(f"Username is valid, welcome {username}")

print(username)
