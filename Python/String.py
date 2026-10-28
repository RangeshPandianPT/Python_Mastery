#Python - Slicing Strings
b = "Hello, World!"
print(b[2:5])

#Slice From the Start
b = "Hello, World!"
print(b[:5])

#Slice To the End
b = "Hello, World!"
print(b[2:])

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

#Python - Modify Strings
#Upper Case
a = "Hello, World!"
print(a.upper())

#Lower Case
a = "Hello, World!"
print(a.lower())

#Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

#Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Python - String Concatenation
#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#Example
#To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Python - Format - Strings
#F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)

#Example-1
#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Example-2
#Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)

#Python - Escape Characters
#Example
#The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."

