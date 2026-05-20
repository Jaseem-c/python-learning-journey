a = "Hello"
print(a)

# multi line string
a = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
print(a)
print("-" * 20)

# strings are arrays
a = "Hello, World!"
print(a[1])
for x in "banana":
    print(x)

print("-" * 20)

# string length
a = "Hello, World!"
print(len(a))
print("-" * 20)

# check string
txt = "The best things in life are free!"
print("free" in txt)
print("expensive" in txt)
print("-" * 20)

# check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)
print("free" not in txt)
print("-" * 20)

# slicing
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print("-" * 20)

# strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())
print("-" * 20)

# lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
print("-" * 20)

# upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
print("-" * 20)

# replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("World", "Jaseem"))
print("-" * 20)

# split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))
print("-" * 20)

# string concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)
print("-" * 20)

# string format
age = 36
txt = "My name is John, and I am {} and I am {} years old."
print(txt.format(age, age))
mark = 56
txt = f"i got {mark} marks in the exam"
print(txt)
print("-" * 20)

# placeholder && modifiers
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
print("-" * 20)

# escape characters
txt = 'We are the so-called "Vikings" from the north.'
print(txt)
