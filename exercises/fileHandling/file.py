# open()	Open file
# read()	Read content
# write()	Write content
# append()	Add new content
# close()	Close file

# Mode	Meaning
# "r"	Read
# "w"	Write (overwrites)
# "a"	Append
# "x"	Create new file
# "rb"	Read binary
# "wb"	Write binary
# Why close() Matters :Files use system resources.
# Closing:frees memory/resources,prevents file locking issues

f = open("test.txt")
print(f.read())
print(f.read(5))
print("-" * 20)
f.close()

# with statement automatically closes the file after the block is executed
with open("test.txt") as f:
    print(f.read())
print("-" * 20)
# readline() method reads one line at a time
with open("test.txt") as f:
    print(f.readline())

# write() method writes a string to the file - creates file if it doesn't exist, overwrites if it does
with open("test.txt", "w") as f:
    f.write("Hello, World!")
print("-" * 20)
# append() method adds new content to the end of the file without overwriting
with open("test.txt", "a") as f:
    f.write("\nWelcome to Python file handling!")

# example
# note = input("Enter note: ")
# with open("notes.txt", "a") as file:
#     file.write(note + "\n")
# print("Saved")

# existing file content
import os
from pathlib import Path

if os.path.exists("notes.txt"):
    # delete
    # os.remove("notes.txt")
    with open("notes.txt", "r") as file:
        print(file.read())
print("-" * 20)

# pathlib module - provides an object-oriented interface for working with file paths. It allows you to manipulate file paths in a more intuitive way, and it also provides methods for checking if a file exists, creating directories, and more.
# pathlib mainly handles paths better, not file reading
P = Path("notes.txt")
print(P.exists())
# read
print(P.read_text(encoding="utf-8"))

# read json file
import json

data = {"name": "Jaseem", "skills": ["Python", "SQL"]}
with open("user.json", "w") as f:
    json.dump(data, f, indent=2)

with open("user.json", "r") as f:
    data = json.load(f)
print(data)

# csv file handling
import csv

with open("scores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerow(["Ali", 90])
