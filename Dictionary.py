#Python Dictionaries

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

"""
Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
"""

#ExampleGet your own Python Server
#Create and print a dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

#Example
#Print the "brand" value of the dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

#Duplicates Not Allowed
#Dictionaries cannot have two items with the same key:

#Example
#Duplicate values will overwrite existing values:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)
print(len(thisdict))
print(type(thisdict))

#Example
#Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Python - Access Dictionary Items

#ExampleGet your own Python Server
#Get the value of the "model" key:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
x = thisdict.get("model")

#Get Keys
#The keys() method will return a list of all the keys in the dictionary.

#Example
#Get a list of the keys:

x = thisdict.keys()

#Example
#Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

#Change Values
#You can change the value of a specific item by referring to its key name:

#ExampleGet your own Python Server
#Change the "year" to 2018:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

#Example
#Update the "year" of the car by using the update() method:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})

#ExampleGet your own Python Server
#The pop() method removes the item with the specified key name:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

#Example
#The del keyword removes the item with the specified key name:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

#Example
#The clear() method empties the dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

#Python - Loop Dictionaries
for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x, y in thisdict.items():
    print(x, y)

#Example
#Make a copy of a dictionary with the dict() function:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Python - Nested Dictionaries

#ExampleGet your own Python Server
#Create a dictionary that contain three dictionaries:

myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}

child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}