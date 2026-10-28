#Python While Loops

#ExampleGet your own Python Server
#Print i as long as i is less than 6:

i = 1
while i < 6:
    print(i)
    i += 1

#The break Statement
#With the break statement we can stop the loop even if the while condition is true:

#Example
#Exit the loop when i is 3:

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#Example
#Continue to the next iteration if i is 3:

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#Example
#Print a message once the condition is false:

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#Python For Loops

#ExampleGet your own Python Server
#Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#Example
#Loop through the letters in the word "banana":

for x in "banana":
    print(x)

#The break Statement
#With the break statement we can stop the loop before it has looped through all the items:

#Example
#Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#Example
#Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#Example
#Using the range() function:

for x in range(6):
    print(x)