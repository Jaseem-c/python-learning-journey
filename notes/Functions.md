# Functions

> Notes from: `exercises/functions/`  
> Reusable blocks of code — DRY principle.

---

## 1. Defining & Calling

```python
def my_function():
    print("Hello from a function")

my_function()

def get_greeting():
    return "Hello from a function"

greeting = get_greeting()
```

- `return` sends a value back (default: `None`).
- Function names use `snake_case`.

---

## 2. Parameters

```python
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")
```

### Default values

```python
def my_function(country="Norway"):
    print("I am from " + country)

my_function("Sweden")  # positional override
my_function()          # uses default
```

### `*args` — variable positional arguments

```python
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")  # tuple inside
```

### `**kwargs` — variable keyword arguments

```python
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname="Tobias", lname="Refsnes")  # dict inside
```

### Practical example — sum any numbers

```python
def total_sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

total_sum(1, 2, 3, 4, 5)
```

**Order rule:** `def f(a, b=0, *args, **kwargs)` — normal → defaults → `*args` → `**kwargs`.

---

## 3. Lambda Functions

Anonymous one-expression functions.

```python
x = lambda a: a + 10
print(x(5))   # 15
```

Often used with higher-order functions:

```python
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))
evens   = list(filter(lambda x: x % 2 == 0, numbers))
above_3 = list(filter(lambda x: x > 3, numbers))

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])  # sort by age
```

| Function | Purpose |
|----------|---------|
| `map(fn, iterable)` | Apply `fn` to each item |
| `filter(fn, iterable)` | Keep items where `fn` returns True |
| `sorted(iterable, key=fn)` | Sort with custom key |

---

## 4. Decorators

A function that **wraps** another function to add behavior without changing its source.

```python
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfn():
    return "hello world"

print(myfn())   # "HELLO WORLD"
```

With arguments:

```python
def changecase(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return myinner

@changecase
def myfunction(nam):
    return "Hello " + nam

print(myfunction("John"))   # "HELLO JOHN"
```

`@decorator` is syntactic sugar for: `myfn = changecase(myfn)`.

---

## 5. Function Metadata

```python
def meta():
  return "Have a great day!"

print(meta.__name__)   # 'meta'
```

Use docstrings for documentation:

```python
def add(a, b):
    """Return sum of a and b."""
    return a + b
```

---

## 6. Recursion

A function that calls itself. Must have:

1. **Base case** — stops recursion  
2. **Recursive case** — calls itself with smaller input  

```python
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)   # 5! = 120
```

---

## Additional Notes (Beyond Basics)

### Unpacking when calling functions

```python
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
add(*nums)              # unpack list as positional args

kwargs = {"a": 1, "b": 2, "c": 3}
add(**kwargs)           # unpack dict as keyword args
```

### Keyword-only arguments (Python 3+)

```python
def create_user(name, *, email, age=18):
    # email must be passed by name: create_user("Ali", email="a@b.com")
    pass
```

### `functools` — common decorator tools

```python
from functools import wraps, lru_cache

def my_decorator(func):
    @wraps(func)          # preserves func.__name__, __doc__
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)   # memoized — much faster
```

### Generators (`yield`)

Memory-efficient — produce values one at a time:

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)
```

Generator expression: `(x**2 for x in range(10))` — lazy, like list comp but with `()`.

### `reduce()` (from functools)

```python
from functools import reduce
reduce(lambda a, b: a + b, [1, 2, 3, 4])   # 10
```

Prefer `sum()` for addition; `reduce` for custom accumulators.

### First-class functions

Functions are objects — pass them around:

```python
def apply(fn, x):
    return fn(x)

apply(lambda n: n * 2, 5)   # 10
```

---

## Quick Reference

| Concept | Syntax |
|---------|--------|
| Define | `def name(params):` |
| Return | `return value` |
| Var args | `*args` |
| Var kwargs | `**kwargs` |
| Lambda | `lambda x: x * 2` |
| Decorator | `@wrapper` above `def` |
| Generator | `yield value` |
| Cache | `@lru_cache` |

---

## Interview Q&A — Functions

**Q1: What is the difference between `*args` and `**kwargs`?**  
**A:** `*args` collects extra **positional** arguments as a tuple. `**kwargs` collects extra **keyword** arguments as a dict.

**Q2: What is a decorator?**  
**A:** A callable that takes a function and returns a new function (often wrapping the original) to add logging, timing, auth, etc.

**Q3: Lambda vs `def` — when to use lambda?**  
**A:** Use `lambda` for short, throwaway functions (e.g. `key=` in `sorted`). Use `def` for anything multi-line or reused.

**Q4: Explain recursion and its risks.**  
**A:** Recursion solves problems by breaking them into smaller subproblems. Risks: hitting recursion limit (`RecursionError`), stack overflow, and sometimes worse performance than iteration. Always define a base case.

**Q5: What does a function return if there is no `return`?**  
**A:** `None`.

**Q6: Pass by value or pass by reference in Python?**  
**A:** Python is “pass by object reference.” Names bind to objects; reassigning a parameter does not affect the caller, but mutating a mutable object (list, dict) inside a function **does** affect the caller's object.

**Q7: What is `map()` vs list comprehension?**  
**A:** Both transform iterables. List comprehensions are more Pythonic and readable: `[x**2 for x in numbers]` vs `list(map(lambda x: x**2, numbers))`.

**Q8: What is a closure?**  
**A:** An inner function that remembers variables from its enclosing scope even after the outer function has finished. Decorators use closures.

**Q9: Generator vs list — when to use generator?**  
**A:** Generators yield items lazily (one at a time, low memory). Use for large/infinite sequences. Lists store everything in memory — fine for small data.

**Q10: What does `@wraps` do in decorators?**  
**A:** Copies metadata (`__name__`, `__doc__`) from the original function to the wrapper so debugging and docs stay correct.
