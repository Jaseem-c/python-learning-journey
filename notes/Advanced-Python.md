# Advanced Python Concepts

> Additional topic — level up after fundamentals  
> Generators, iterators, comprehensions, decorators patterns, and idioms.

---

## 1. Iterators vs Generators

**Iterable** — can be looped (`list`, `str`, `dict`)  
**Iterator** — object with `__iter__()` and `__next__()`

```python
nums = iter([1, 2, 3])
next(nums)   # 1
next(nums)   # 2
```

**Generator** — iterator built with `yield`:

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
next(gen)   # 0
next(gen)   # 1
```

---

## 2. Comprehensions Cheat Sheet

```python
[x * 2 for x in range(5)]
[x for x in range(10) if x % 2 == 0]
{x: x**2 for x in range(5)}
{x for x in "hello"}
(x**2 for x in range(1000000))   # generator — lazy
```

Nested (use sparingly — readability):

```python
matrix = [[i * j for j in range(3)] for i in range(3)]
```

---

## 3. `itertools` (sampling)

```python
import itertools

list(itertools.chain([1, 2], [3, 4]))       # [1, 2, 3, 4]
list(itertools.combinations("ABC", 2))      # ('A','B'), ...
list(itertools.permutations([1, 2], 2))
list(itertools.islice(range(100), 5, 10))   # [5,6,7,8,9]
```

---

## 4. Decorator Patterns

### With arguments

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi")
```

### Class-based decorator

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)
```

---

## 5. Context Managers & `contextlib`

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    def __exit__(self, *args):
        print(f"Elapsed: {time.time() - self.start:.2f}s")

with Timer():
    sum(range(1_000_000))
```

```python
from contextlib import contextmanager

@contextmanager
def temp_change(obj, attr, value):
    old = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield
    finally:
        setattr(obj, attr, old)
```

---

## 6. `*args` unpacking in practice

```python
def log(level, message):
    print(f"[{level}] {message}")

config = ("ERROR", "Disk full")
log(*config)
```

---

## 7. Pythonic Idioms

```python
# Swap
a, b = b, a

# Default dict value
counts = {}
counts[key] = counts.get(key, 0) + 1

# Ternary
status = "adult" if age >= 18 else "minor"

# Any / all
any(x > 10 for x in nums)
all(x > 0 for x in nums)

# Enumerate zip
for i, (name, score) in enumerate(zip(names, scores)):
    print(i, name, score)
```

---

## 8. `__main__` and scripting

Structure projects as:

```text
project/
  src/
    myapp/
      __init__.py
      main.py
  tests/
  requirements.txt
```

---

## Interview Q&A — Advanced Python

**Q1: Iterator vs generator?**  
**A:** Generator is a type of iterator created with `yield` or generator expressions. Simpler to write than full iterator classes.

**Q2: What is a decorator factory?**  
**A:** A function that returns a decorator — used when decorator needs configuration (`@repeat(3)`).

**Q3: What is the GIL?**  
**A:** Global Interpreter Lock — CPython allows one thread to execute Python bytecode at a time. CPU-bound parallelism uses `multiprocessing`; I/O-bound uses `threading` or `asyncio`.

**Q4: List vs generator comprehension for 1M items?**  
**A:** Generator uses O(1) memory; list uses O(n). Use generator for pipelines and large data.

**Q5: What is `__call__` on a class?**  
**A:** Makes instances callable like functions: `obj()`. Used in callable classes and some decorators.
