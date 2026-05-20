# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# raise Manually create error

# Exception	Meaning
# ValueError	Wrong value type
# ZeroDivisionError	Divide by zero
# FileNotFoundError	File missing
# IndexError	Invalid list index
# KeyError	Missing dictionary key
# TypeError	Wrong data type operation

try:
    num = int(input("Enter number: "))
    print(num)
except:
    print("Invalid input. Please enter a number.")
# except NameError:
#   print("Variable x is not defined")
else:
    print("Input is valid.")
finally:
    print("The 'try except' is finished")

# raise ("This is a custom error message")
val = int(input("Enter value: "))
if val < 0:
    raise Exception("Negative value is not allowed")

# write alsways the specific error you want to catch - not generic exception
