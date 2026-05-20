class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class student(Person):
    def __init__(self, fname, lname, age):
        # super().__init__(fname, lname)
        Person.__init__(self, fname, lname)
        self.age = age


x = Person("John", "Doe")
x.printname()
y = student("Mike", "Olsen", 20)
y.printname()
print(y.age)
