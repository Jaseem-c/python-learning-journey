# ordered,unchangeable, allows duplicate members
fruits = ("apple", "banana", "cherry")
print(fruits)
print(fruits[0])
# one item tuple, need comma
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = "apple"
print(type(thistuple))
print("-" * 20)

# add items to a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
print("-" * 20)

# remove items from a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("banana")
thistuple = tuple(y)
print(thistuple)
print("-" * 20)

# delete tuple
thistuple = ("apple", "banana", "cherry")
del thistuple

# loop through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# check if item exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
