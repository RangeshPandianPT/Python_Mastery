#Python Booleans

#Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Example
#Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))

#Example
#Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#True Values
#Example
#The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#Example
#The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Example
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

#Functions can Return a Boolean
#Example
#Print the answer of a function:

def myFunction() :
    return True

print(myFunction())

#Example
#Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

#Example
#Check if an object is an integer or not:

x = 200
print(isinstance(x, int))