# ordered, changeable, allows duplicate members
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(len(fruits))
fruits[1:3] = ["blackcurrant", "watermelon"]
print(fruits)
fruits.append("orange")
print(fruits)
fruits.insert(1, "lemon")
print(fruits)
newlist = ["mango", "pineapple", "papaya"]
fruits.extend(newlist)
print(fruits)
fruits.remove("pineapple")
print(fruits)
fruits.pop(1)
print(fruits)
fruits.clear()
print(fruits)

# loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# check if item exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)
newlist = [x for x in fruits if "a" in x]
print(newlist)
print("-" * 20)
# sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# sort descending
thislist.sort(reverse=True)
print(thislist)
print("-" * 20)

# copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
