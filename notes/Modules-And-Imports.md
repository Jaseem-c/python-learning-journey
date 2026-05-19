# Modules & Imports

> Additional topic — organize code across files and reuse libraries.

---

## 1. What is a Module?

Any `.py` file is a module. Import it to reuse code.

```python
# mymath.py
def add(a, b):
    return a + b

PI = 3.14159
```

```python
# main.py
import mymath
print(mymath.add(2, 3))
print(mymath.PI)

from mymath import add
print(add(2, 3))

from mymath import add as sum_two
```

---

## 2. Packages

A **package** is a folder with `__init__.py` (can be empty).

```text
myproject/
  main.py
  utils/
    __init__.py
    helpers.py
```

```python
from utils.helpers import clean_text
```

---

## 3. `if __name__ == "__main__"`

Runs code only when file is executed directly, not when imported:

```python
def main():
    print("Running as script")

if __name__ == "__main__":
    main()
```

---

## 4. Standard Library Highlights

| Module | Use |
|--------|-----|
| `os` / `pathlib` | Filesystem |
| `sys` | Interpreter args, exit |
| `datetime` | Dates and times |
| `json` | JSON |
| `random` | Random numbers |
| `math` | Math functions |
| `re` | Regular expressions |
| `itertools` | Iterator tools |
| `collections` | Specialized containers |

```python
from datetime import datetime, timedelta

now = datetime.now()
tomorrow = now + timedelta(days=1)

import random
random.randint(1, 10)
random.choice(["a", "b", "c"])
```

---

## 5. Third-Party Packages — `pip`

```bash
pip install requests
pip install pandas
pip list
pip freeze > requirements.txt
pip install -r requirements.txt
```

Install into a **virtual environment** (see Environment-And-Tools.md).

---

## 6. `__all__` — control `from module import *`

```python
# mymodule.py
__all__ = ["public_func"]

def public_func():
    pass

def _internal():
    pass
```

Avoid `import *` in production code — explicit imports are clearer.

---

## Interview Q&A — Modules

**Q1: Difference between `import module` and `from module import name`?**  
**A:** `import module` namespaces as `module.name`. `from module import name` brings `name` into current namespace directly.

**Q2: What does `if __name__ == "__main__"` do?**  
**A:** `__name__` is `"__main__"` when file is run directly; otherwise it's the module name. Guards script-only code from running on import.

**Q3: What is `requirements.txt`?**  
**A:** List of packages and versions for reproducible installs: `pip install -r requirements.txt`.

**Q4: Relative vs absolute import?**  
**A:** Absolute: `from utils.helpers import fn`. Relative (inside package): `from .helpers import fn` or `from ..other import x`.

**Q5: What is a namespace?**  
**A:** Mapping of names to objects. Each module has its own namespace; imports add names to the current namespace.
