OOP groups:data related behavior into one structure.
Provides a clear structure to programs
Makes code easier to maintain, reuse, and debug
Helps keep your code DRY (Don't Repeat Yourself)

Core OOP Concepts
Main concepts:
Class
Object
Constructor
Attributes
Methods
Inheritance
Encapsulation
Polymorphism
Abstraction

class:-
A class defines what an object should look like, and an object is created based on that class
A class is a blueprint/template.
Example:
“Car” is a class
Actual cars are objects

objects:-
An object is a real instance created from a class.
Example:BMW car,Tesla car

self - The current object using the method.
Is always the first parameter of any instance method
Lets the object refer to its own attributes and methods
Without self, Python would not know which object's properties you want to access:
constructor
init constructor- This runs automatically when object is created.
A constructor is a special method that gets called automatically when you create an object from a class. In Python, the constructor is the __init__ method.
Is used to set up initial values (attributes) for the object


Inheritance
one class can reuse another class.
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
Without inheritance:repeated code,harder maintenance
With inheritance:reuse common behavior

polymorphism
The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
for eg len(), string - number of characters while in tuples it gives number of elements

encapsulation
Encapsulation is about protecting data inside a class.
It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
This prevents accidental changes to your data and hides the internal details of how your class works.
In Python, you can make properties private by using a double underscore __ prefix:
Python also has a convention for protected properties using a single underscore _ prefix:

Data Protection: Prevents accidental modification of data
Validation: You can validate data before setting it
Flexibility: Internal implementation can change without affecting external code
Control: You have full control over how data is accessed and modified

abstarction
Hiding internal implementation details and showing only the essential features to the user.
Python provides abstraction support using: ABC Class - abstract base class
Abstraction in Python means hiding implementation details and showing only essential functionality to the user.
It is mainly achieved using abstract classes and abstract methods from the abc module.
abstract classes cannot be instantiated directly
Abstraction in Python means hiding internal implementation details and exposing only required functionality. Python achieves abstraction using abstract classes and abstract methods from the abc module. Abstract classes act as blueprints, and child classes must implement the abstract methods.