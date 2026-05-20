# any .py files - a Python file containing reusable code.
# Module	Purpose
# math	Mathematical functions
# random	Random values
# os	Operating system
# json	JSON handling
# csv	CSV handling
# pathlib	File paths

import mymath, math

print(mymath.add(5, 3))
print(mymath.PI)
print(math.sqrt(16))
from mymath import add as sum_two

print(sum_two(10, 20))

# packages - a way of structuring Python’s module namespace by using “dotted module names”. A package is a collection of modules in directories that give a package hierarchy.
# A directory must contain a file named __init__.py in order for Python to consider it as a package. This file can be empty, but it can also execute initialization code for the package or set the __all__ variable to define the public interface of the package.
# To import a module from a package, you can use the dot notation. For example, if you have a package named mypackage and a module named mymodule inside that package, you can import it like this:

from mypackage.sum import addNum

print(addNum(10, 20))

# __name__ == "__main__"
# When a Python file is run directly, the special variable __name__ is set to "__main__". This allows you to check if the file is being run directly or imported as a module in another file. If the file is being run directly, you can execute some code, such as a test or a demo, without it being executed when the file is imported as a module.
# For example, you can add the following code at the end of your module to test its functionality:

# if __name__ == "__main__":
# this code runs ONLY when you directly run this file
# it will NOT run if this file is imported by another file
if __name__ == "__main__":
    print("This code is being run directly")
    print(addNum(5, 3))
else:
    print("This code is being imported as a module")

# thirdparty packages - numpy,pandas,matplotlib,requests,flask,django
# pip - Pip Installs Packages (python package installer like npm for nodejs)
# Install a package
# pip install numpy

# # Install a specific version
# pip install numpy==1.24.0

# # Uninstall a package
# pip uninstall numpy

# # Upgrade a package
# pip install --upgrade numpy

# # See all installed packages
# pip list

# # Search what version is installed
# pip show numpy

# Dunder Methods-Double underscore on both sides
# __all__      →  dunder all
# __init__     →  dunder init
# __name__     →  dunder name
# __main__     →  dunder main
# __all__ :- control from module import *
from mymath import *

print(add(5, 3))
print(subtract(10, 5))  # This will raise an error because subtract is


def greet(name, age):
    print("Hello " + name + "you are " + str(age) + "years old")


x = {"name": "Ravi", "age": 25, "city": "Bangalore"}
