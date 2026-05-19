# Object-Oriented Programming (OOP)

> Notes from: `exercises/oops/`  
> OOP groups **data + behavior** into one structure — easier to maintain, reuse, and debug (DRY).

---

## Why OOP?

| Without OOP | With OOP |
|-------------|----------|
| Repeated code | Reuse via inheritance |
| Hard to maintain | Clear structure (classes) |
| Scattered logic | Encapsulated units |

---

## Core Building Blocks

| Term | Meaning |
|------|---------|
| **Class** | Blueprint / template |
| **Object** | Real instance of a class |
| **`__init__`** | Constructor — runs on creation |
| **Attributes** | Data stored on object (`self.name`) |
| **Methods** | Functions inside a class |
| **`self`** | Reference to current instance |

---

## 1. Class & Object

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name)
        print(self.marks)

s1 = Student("John", 85)
s1.show()
```

- **Class** = “Car” (blueprint)  
- **Object** = BMW, Tesla (actual instances)  
- **`self`** is always the first parameter of instance methods — binds the method to the object.

---

## 2. Constructor (`__init__`)

Runs **automatically** when you create an object. Sets initial attribute values.

```python
def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
```

Other special methods (know for interviews):

| Method | Purpose |
|--------|---------|
| `__str__` | Human-readable string (`print(obj)`) |
| `__repr__` | Developer representation |
| `__len__` | `len(obj)` |

---

## 3. Inheritance

Child class reuses parent class behavior.

```python
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, age):
        Person.__init__(self, fname, lname)   # call parent
        # super().__init__(fname, lname)      # preferred style
        self.age = age


x = Person("John", "Doe")
y = Student("Mike", "Olsen", 20)
```

| Term | Also called |
|------|-------------|
| Parent / base | superclass |
| Child / derived | subclass |

**`super()`** — calls parent method without hardcoding class name (better for multiple inheritance).

---

## 4. Polymorphism

**“Many forms”** — same interface, different behavior.

### Built-in example

```python
len("hello")    # 5 characters
len([1, 2, 3])  # 3 elements
```

### Custom example (duck typing)

```python
class Car:
    def move(self):
        print("Drive!")

class Boat:
    def move(self):
        print("Sail!")

class Plane:
    def move(self):
        print("Fly!")

vehicles = [Car(), Boat(), Plane()]
for v in vehicles:
    v.move()   # same method name, different output
```

Python uses **duck typing**: “If it walks like a duck and quacks like a duck, treat it as a duck.” No strict interface required.

---

## 5. Encapsulation

Bundle data + methods; **control access** to internal state.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age      # name mangling → "private"

    def get_age(self):
        return self.__age


p1 = Person("Emil", 25)
print(p1.name)        # OK — public
# print(p1.__age)     # AttributeError
print(p1.get_age())   # OK — controlled access
```

| Convention | Meaning |
|------------|---------|
| `name` | Public |
| `_name` | Protected (convention only) |
| `__name` | Private (name mangling: `_ClassName__name`) |

**Benefits:** validation before set, hide implementation, prevent accidental changes.

### Property decorator (Pythonic encapsulation)

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
```

---

## 6. Abstraction

Hide **how** it works; show **what** it does.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog barks")


d = Dog()
d.sound()
```

```python
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):
    def pay(self):
        print("UPI Payment Successful")
```

- **Abstract class** — cannot instantiate directly; defines a contract.  
- **Abstract method** — must be implemented in child classes.  
- Module: `from abc import ABC, abstractmethod`

---

## Four Pillars Summary

| Pillar | One line |
|--------|----------|
| **Encapsulation** | Hide data, expose safe interface |
| **Abstraction** | Hide complexity, show essentials |
| **Inheritance** | Reuse parent code in child |
| **Polymorphism** | Same action, different implementations |

---

## Additional Notes (Beyond Basics)

### Magic (dunder) methods — common ones

| Method | Triggered by |
|--------|--------------|
| `__init__` | Object creation |
| `__str__` | `print(obj)`, `str(obj)` |
| `__repr__` | REPL, `repr(obj)` — aim for valid recreate string |
| `__len__` | `len(obj)` |
| `__eq__` | `obj1 == obj2` |
| `__lt__` etc. | Sorting comparisons |
| `__getitem__` | `obj[key]` |
| `__enter__` / `__exit__` | `with` statement |

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"

    def __len__(self):
        return self.pages
```

### Dataclasses (Python 3.7+) — less boilerplate

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    marks: int

s = Student("John", 85)   # auto __init__, __repr__, __eq__
```

### Multiple inheritance & MRO

```python
class A:
    def greet(self):
        return "A"

class B(A):
    def greet(self):
        return "B"

class C(A):
    pass

class D(B, C):
    pass

D.__mro__   # method lookup order: D → B → C → A → object
```

Always call `super()` in cooperative multiple inheritance.

### `__slots__` — memory optimization

```python
class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

Fixes attribute set — no `__dict__` per instance. Use when you have millions of small objects.

### Singleton pattern (simple)

```python
class Database:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### SOLID principles (interview topic)

| Letter | Idea |
|--------|------|
| **S** | Single Responsibility — one class, one job |
| **O** | Open/Closed — open for extension, closed for modification |
| **L** | Liskov Substitution — child usable wherever parent is |
| **I** | Interface Segregation — small focused interfaces |
| **D** | Dependency Inversion — depend on abstractions, not concretions |

---

## Quick Reference

```python
class MyClass(Parent):           # inheritance
    class_var = 0                # shared by all instances

    def __init__(self, x):
        self.x = x               # instance attribute

    def method(self):            # instance method
        return self.x

    @classmethod
    def from_string(cls, s):     # gets cls, not self
        return cls(int(s))

    @staticmethod
    def helper():                # no self/cls
        return 42
```

---

## Interview Q&A — OOP

**Q1: What are the four pillars of OOP?**  
**A:** Encapsulation, abstraction, inheritance, polymorphism.

**Q2: What is `self` in Python?**  
**A:** A reference to the current instance. Passed explicitly as the first argument of instance methods so the method knows which object's data to use.

**Q3: Difference between class attribute and instance attribute?**  
**A:** Class attribute is shared by all instances (`Class.attr`). Instance attribute belongs to one object (`self.attr`). Changing class attr does not change existing instance attrs unless accessed through the class.

**Q4: What is `super()`?**  
**A:** Returns a proxy to the parent class so you can call parent methods — especially `super().__init__()` in child constructors.

**Q5: Can Python have multiple inheritance?**  
**A:** Yes. A class can inherit from multiple parents. Method Resolution Order (MRO) determines lookup order — use `ClassName.__mro__` or `help(C)`.

**Q6: Abstract class vs interface?**  
**A:** Python has no separate `interface` keyword. Abstract Base Classes (`ABC`) define required methods via `@abstractmethod`. Java interfaces are closer to ABCs with only abstract methods.

**Q7: Does Python have true private variables?**  
**A:** No. `__attr` uses name mangling (`_ClassName__attr`) — convention + slight obfuscation, not security. Single `_` is “protected by convention.”

**Q8: What is polymorphism in Python?**  
**A:** Same method name behaves differently per class (method overriding) or built-ins (`len`, `+`) work on many types. Python favors duck typing over strict interfaces.

**Q9: `@classmethod` vs `@staticmethod` vs instance method?**  
**A:** Instance method gets `self` (instance). Classmethod gets `cls` (class) — useful for alternative constructors. Staticmethod gets neither — utility function namespaced in class.

**Q10: What is duck typing?**  
**A:** Type is determined by behavior (methods/attributes), not inheritance. If an object has `move()`, you can use it in a loop with other “movable” objects.

**Q11: Why use abstraction with ABC?**  
**A:** Forces subclasses to implement required methods; prevents instantiating incomplete classes; documents a contract (e.g. all `Payment` types must implement `pay()`).

**Q12: Composition vs inheritance?**  
**A:** Inheritance IS-A (`Dog` is `Animal`). Composition HAS-A (`Car` has an `Engine`). Favor composition when behavior should not be tightly coupled to a hierarchy — “favor composition over inheritance.”

**Q13: What is a dataclass?**  
**A:** A decorator `@dataclass` that auto-generates `__init__`, `__repr__`, `__eq__` for data-holding classes — less boilerplate than manual classes.

**Q14: What is MRO?**  
**A:** Method Resolution Order — the order Python searches base classes when you call a method. View with `ClassName.__mro__` or `help(ClassName)`.
