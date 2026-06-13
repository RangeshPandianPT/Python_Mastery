#Example
#Checking if a number is positive:

number = 15
if number > 0:
    print("The number is positive")

#Example
#Checking if a number is positive:

number = 15
if number > 0:
    print("The number is positive")


#ExampleGet your own Python Server
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")


#Example
#Testing multiple conditions:

score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")


#Example
#Categorizing age groups:

age = 25

if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are a senior")

#ExampleGet your own Python Server
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#Example
#Temperature classifier:

temperature = 22

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's warm outside")
elif temperature > 10:
    print("It's cool outside")
else:
    print("It's cold outside!")

#Python Nested If
#ExampleGet your own Python Server
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

#Example
#Checking multiple conditions with nesting:

age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")

#Example
#Three levels of nesting:

score = 85
attendance = 90
submitted = True

if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("Pass but low attendance")
else:
    print("Fail")

#Example
#Placeholder for future implementation:

age = 16

if age < 18:
    pass # TODO: Add underage logic later
else:
    print("Access granted")

    