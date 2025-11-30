x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z: float = float(3)  # z will be 3.0

print(type(x))
print(type(y))

#Case-Sensitive
a = 4
A = "Sally"
#A will not overwrite a

#Python - Variable Names
#Camel Case
myVariableName = "John"

#Snake Case
my_variable_name = "John"

#Pascal Case
MyVariableName = "John"

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)

#Global Variables
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

#Example
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

#The global Keyword
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
