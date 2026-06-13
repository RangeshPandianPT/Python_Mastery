a = 10
b= 3

#Arithmetic operator
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b) #10*10*10
print (a//b)

#Comparision operator
x= 5
y = 10

print(x==y)
print(x!=y)
print(x<y)
print(x>y)

#Logical Operator
g = True
v = False

print (g and v) # replace->  print (g & v)
print (g or v) #replace -> print (g | v)
print (not g)
print (not v)

#Example Code-1
amount= 1200
tax = amount * 0.18
total = amount + tax
print(total)

if total > 100:
    discount = total * 0.10
    total -= discount
print(total)

#Example Code-2
age = 65
student = 'yes'

if age >= 60 or student == 'yes':
    print("Discount Applicable")
else:
    print("Not Applicable")

#Python Comments
""" This is a multiline command 
thus is very cool for understanding """