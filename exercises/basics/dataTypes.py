"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

x = ["apple", "banana", "cherry"]
y = ("apple", "banana", "cherry")
z = range(6)
a = {"name": "John", "age": 36}
b = {"apple", "banana", "cherry"}
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print("-" * 20)

# specific data type
x = list(("apple", "banana", "cherry"))
y = dict(name="John", age=36)
z = set(("apple", "banana", "cherry"))
print(x)
print(y)
print(z)
