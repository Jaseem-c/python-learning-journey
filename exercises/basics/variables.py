x = 5
y = "John"
print(x)
print(y)
print(type(x))
print(type(y))
print("-"*20)

#casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)
print("-"*20)

#multiple assignment
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print("-"*20)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print("-"*20)

#Global Variables
x = "awesome"
def myfunc():
  global x 
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)