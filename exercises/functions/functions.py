def my_function():
    print("Hello from a function")


my_function()


def get_greeting():
    return "Hello from a function"


greeting = get_greeting()
print(greeting)


# function with parameters
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")


# default parameter value
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function()


# Arbitrary Arguments - *args - if you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# Keyword Arguments - **kwargs - if you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


def total_sum(*numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total


print(total_sum(1, 2, 3, 4, 5))
print(total_sum(10, 20, 30))


# decorators - a function that takes another function as an argument, adds some kind of functionality and returns another function without modifying the original function.
# Decorators let you add extra behavior to a function, without changing the function's code.
def changecase(func):
    def myinner():
        return func().upper()

    return myinner


@changecase
def myfn():
    return "hello world"


print(myfn())


# with arguements
def changecase(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return myinner


@changecase
def myfunction(nam):
    return "Hello " + nam


print(myfunction("John"))


# meta data
def meta():
    return "Have a great day!"


print(meta.__name__)

# lambda function - a small anonymous function that can take any number of arguments, but can only have one expression. It is often used as an argument to higher-order functions, such as map(), filter(), and reduce().
x = lambda a: a + 10
print(x(5))

# map(),reduce(), filter(),sorted() - higher-order functions that take a function as an argument and apply it to a sequence of elements.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
reduced = list(filter(lambda x: x % 2 == 0, numbers))
print(reduced)
filtered = list(filter(lambda x: x > 3, numbers))
print(filtered)
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
