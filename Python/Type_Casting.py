#Type Casting

x = "10"
y = '1'

print ( x+ y) #concat happens
print (int(x)+int(y)) #Casted to int

a = int(x)
print(type(x))
print(type(a))
print(type(y))

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

print(type(str(x)))