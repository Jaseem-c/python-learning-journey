# class Student:
#     def greet(self):
#         print("Hello Student")

# s1 = Student()
# s1.greet()


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name)
        print(self.marks)


s1 = Student("John", 85)
s1.show()
