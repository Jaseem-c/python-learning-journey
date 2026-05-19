#unordered, unindexed, no duplicate values, unchangeable(can add/remove items)
thisset = {"apple", "banana", "cherry","apple"}
print(thisset)
print(type(thisset))
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#loop through a set(can only access items through a loop)
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
#check if item exists
thisset = {"apple", "banana", "cherry"}
if "banana" in thisset:
    print("Yes, 'banana' is in the fruits set") 
print("-"*20)

#add items to a set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
thisset.update(["mango", "grapes"])
print(thisset)
print("-"*20)

#remove items from a set
thisset = {"apple", "banana", "cherry","orange", "mango", "grapes"}
thisset.remove("banana") #if item doesn't exist, it will raise an error
print(thisset)
thisset.discard("banana") #if item doesn't exist, it will NOT raise an error
print(thisset)
thisset.pop() #removes a random item
thisset.clear() #empties the set
print(thisset)
del thisset #deletes the set
print("-"*20)

#loop through a set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
#only for loop can access items in a set, cannot access through index
print("-"*20)

#union of sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set4 = set1 | set2
print(set4)
print("-"*20)
#intersection of sets
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set3 = set1.intersection(set2)
print(set3)
set4 = set1 & set2
print(set4)
print("-"*20)

#difference of sets
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set3 = set1.difference(set2)
print(set3)
set4 = set1 - set2
print(set4)
print("-"*20)