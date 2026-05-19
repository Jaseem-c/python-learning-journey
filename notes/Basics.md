# Python Basics

> Notes from: `exercises/basics/`  
> Goal: variables, types, casting, and how Python stores values.

---

## 1. Hello World & Comments

```python
print("Hello, World!")

# Single-line comment

"""
Multi-line comment (docstring style).
Used for longer explanations.
"""
```

| Type | Syntax | Use |
|------|--------|-----|
| Single-line | `#` | Short notes |
| Multi-line | `""" ... """` | Blocks of explanation |

---

## 2. Variables

- No type declaration — assign and Python infers the type.
- Names are case-sensitive: `age` ≠ `Age`.

```python
x = 5
y = "John"
print(type(x))   # <class 'int'>
print(type(y))   # <class 'str'>
```

### Multiple assignment

```python
x, y, z = "Orange", "Banana", "Cherry"

fruits = ["apple", "banana", "cherry"]
a, b, c = fruits   # unpack collection
```

### Type casting

| Function | Converts to |
|----------|-------------|
| `int()` | integer |
| `float()` | float |
| `str()` | string |

```python
x = str(3)    # '3'
y = int(3)    # 3
z = float(3)  # 3.0
```

### Global variables

Use `global` inside a function to modify a module-level variable.

```python
x = "awesome"

def myfunc():
    global x
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)   # both print "fantastic"
```

---

## 3. Built-in Data Types (Overview)

| Category | Types | Mutable? |
|----------|-------|----------|
| Text | `str` | No (immutable) |
| Numeric | `int`, `float`, `complex` | — |
| Sequence | `list`, `tuple`, `range` | list yes, tuple no |
| Mapping | `dict` | Yes |
| Set | `set`, `frozenset` | set yes, frozenset no |
| Boolean | `bool` | — |
| Binary | `bytes`, `bytearray` | bytearray yes |
| None | `NoneType` | — |

```python
x = ["apple", "banana", "cherry"]   # list
y = ("apple", "banana", "cherry")   # tuple
z = range(6)                        # range
a = {"name": "John", "age": 36}     # dict
b = {"apple", "banana", "cherry"}   # set

# Explicit constructors
x = list(("apple", "banana", "cherry"))
y = dict(name="John", age=36)
z = set(("apple", "banana", "cherry"))
```

---

## Additional Notes (Beyond Basics)

### `nonlocal` — modify enclosing (not global) scope

```python
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

counter = outer()
counter()  # 1
counter()  # 2
```

Use `global` for module level; `nonlocal` for nested functions.

### Truthiness & short-circuit

```python
# Falsy: False, None, 0, 0.0, "", [], {}, set()
if name:          # better than if name != ""
    print(name)

# and / or stop early
result = a or b   # first truthy value
result = a and b  # first falsy or last value
```

### Walrus operator `:=` (Python 3.8+)

Assign and use in one expression:

```python
if (n := len(data)) > 10:
    print(f"List has {n} items")
```

### Type hints (optional but common in jobs)

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

age: int = 25
scores: list[float] = [90.5, 88.0]
```

Hints do not enforce types at runtime — use `mypy` or IDE for checking.

### Numbers — useful extras

```python
10 / 3    # 3.333... float division
10 // 3   # 3        floor division
10 % 3    # 1        modulo
2 ** 10   # 1024     power

int("1010", 2)   # binary string → 10
bin(10)          # '0b1010'
hex(255)         # '0xff'
```

### Identity vs equality (deep dive)

```python
a = [1, 2]
b = [1, 2]
a == b   # True  — same values
a is b   # False — different objects in memory

x = None
if x is None:    # preferred over == None
    pass
```

### `input()` and basic I/O

```python
name = input("Enter your name: ")   # always returns str
age = int(input("Enter age: "))
```

---

## Quick Reference

| Concept | Remember |
|---------|----------|
| `type()` | Check variable type |
| Casting | `int()`, `float()`, `str()` |
| Unpacking | `a, b, c = [1, 2, 3]` |
| `global` | Modify module-level variable |
| `nonlocal` | Modify enclosing function variable |
| `is` vs `==` | Identity vs value |

---

## Interview Q&A — Basics

**Q1: Is Python statically or dynamically typed?**  
**A:** Dynamically typed. You do not declare types; types are checked at runtime. A variable can be reassigned to a different type.

**Q2: Difference between `=` and `==`?**  
**A:** `=` assigns a value. `==` compares two values for equality.

**Q3: What is `None` in Python?**  
**A:** `None` is a singleton object meaning “no value.” Its type is `NoneType`. Often used as a default return when a function returns nothing explicitly.

**Q4: Mutable vs immutable — give examples.**  
**A:** Immutable: `int`, `float`, `str`, `tuple`. Mutable: `list`, `dict`, `set`. Immutable objects cannot be changed in place; operations create new objects.

**Q5: What does `global` do?**  
**A:** It tells Python that a name inside a function refers to the global (module-level) variable, so assignment updates the global name instead of creating a local one.

**Q6: How do you convert `"42"` to integer 42?**  
**A:** `int("42")`. For floats: `float("3.14")`.

**Q7: What is the difference between `is` and `==`?**  
**A:** `==` compares values. `is` compares identity (same object in memory). Use `==` for value equality; `is` mainly for `None` checks (`x is None`).

**Q8: What is `//` vs `/`?**  
**A:** `/` is true division (float). `//` is floor division (rounds down to integer).

**Q9: What are type hints?**  
**A:** Optional annotations (`name: str`, `-> int`) documenting expected types. Python ignores them at runtime; tools like mypy check them statically.

