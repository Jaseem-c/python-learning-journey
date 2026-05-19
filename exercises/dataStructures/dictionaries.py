#ordered, unindexed, no duplicate values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#accessing items
thisdict = {
  "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])
print(thisdict.get("model"))
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

#change values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2020
print(thisdict)
thisdict.update({"year": 2021})
print(thisdict)
print("-"*20)

#add items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
thisdict["color"] = "red"
print(thisdict)
thisdict.update({"color": "blue"})
print(thisdict)
print("-"*20)

#remove items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red"
    }
thisdict.pop("model")
print(thisdict)
thisdict.popitem() #removes the last inserted item
print(thisdict)
thisdict.clear() #empties the dictionary
print(thisdict)
del thisdict #deletes the dictionary
print("-"*20)

#loop through a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
for x in thisdict:
    print(x) #prints keys
for x in thisdict:
    print(thisdict[x]) #prints values
for x in thisdict.values():
    print(x) #prints values
for x in thisdict.keys():
    print(x) #prints keys
for x, y in thisdict.items():
    print(x, y) #prints keys and values
print("-"*20)

#check if key exists
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
