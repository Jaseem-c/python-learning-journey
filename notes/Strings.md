# Strings in Python

> Notes from: `exercises/basics/strings.py`  
> Strings are **immutable** sequences of characters.

---

## 1. Creating Strings

```python
a = "Hello"
a = """Multi-line
string works too."""
```

- Indexing: `a[1]` → second character (`'e'`)
- Iterable: `for x in "banana": print(x)`
- Length: `len(a)`

---

## 2. Membership & Slicing

```python
txt = "The best things in life are free!"
"free" in txt          # True
"expensive" not in txt # True

b = "Hello, World!"
b[2:5]    # 'llo'   — start 2, end before 5
b[:5]     # 'Hello' — from start
b[2:]     # 'llo, World!' — to end
```

---

## 3. Common Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `strip()` | Remove leading/trailing whitespace | `" Hi ".strip()` → `"Hi"` |
| `lower()` / `upper()` | Case change | `"Hi".upper()` → `"HI"` |
| `replace(old, new)` | Substitute substring | `"World".replace("W","J")` |
| `split(sep)` | Split into list | `"a,b".split(",")` → `['a','b']` |

```python
a = " Hello, World! "
a.strip()
a.lower()
a.upper()
a.replace("World", "Jaseem")
a.split(",")
```

---

## 4. Concatenation & Formatting

```python
# Concatenation (+)
c = "Hello" + " " + "World"

# .format()
age = 36
txt = "My name is John, I am {} years old.".format(age)

# f-strings (preferred)
mark = 56
txt = f"I got {mark} marks in the exam"

# Modifiers
price = 59
f"The price is {price:.2f} dollars"   # 59.00
```

| Style | When to use |
|-------|-------------|
| `+` | Simple joins |
| `.format()` | Legacy / positional templates |
| `f"..."` | Modern, readable, fast |

---

## 5. Escape Characters

```python
txt = "We are the so-called \"Vikings\" from the north."
# \"  \'  \\  \n  \t
```

---

## Additional Notes (Beyond Basics)

### More useful methods

| Method | Purpose |
|--------|---------|
| `startswith()` / `endswith()` | Prefix/suffix check |
| `join(iterable)` | Join list into one string |
| `find()` / `index()` | Find substring (`index` raises if missing) |
| `count(sub)` | Count occurrences |
| `isalpha()`, `isalnum()`, `isspace()` | Character class checks |

```python
", ".join(["apple", "banana"])     # "apple, banana"
"hello world".title()              # "Hello World"
"path/to/file".removesuffix(".py") # Python 3.9+
```

### Raw strings `r"..."`

Backslashes are literal — great for paths and regex:

```python
path = r"C:\Users\name\file.txt"
pattern = r"\d+"
```

### String alignment in f-strings

```python
name = "Ali"
f"{name:>10}"    # right-align, width 10
f"{name:<10}"    # left-align
f"{3.14159:.2f}" # 3.14
f"{1000000:,}"   # 1,000,000
```

### `ord()` and `chr()`

```python
ord('A')   # 65
chr(65)    # 'A'
```

### Regular expressions (intro)

```python
import re

re.search(r"\d+", "Room 42")      # match object or None
re.findall(r"\w+", "hi there")    # ['hi', 'there']
re.sub(r"\s+", "-", "a  b  c")    # 'a-b-c'
```

Use regex when simple `in` / `split` is not enough (emails, phone numbers, logs).

---

## Quick Reference

| Task | Code |
|------|------|
| First char | `s[0]` |
| Last char | `s[-1]` |
| Reverse (trick) | `s[::-1]` |
| Check substring | `"sub" in s` |
| Remove spaces | `s.strip()` |
| Join list | `", ".join(items)` |

---

## Interview Q&A — Strings

**Q1: Are strings mutable in Python?**  
**A:** No. Strings are immutable. Methods like `upper()` return a **new** string; the original is unchanged.

**Q2: What is the difference between `split()` and `partition()`?**  
**A:** `split(sep)` splits on all occurrences into a list. `partition(sep)` splits only on the **first** occurrence into three parts: `(before, sep, after)`.

**Q3: Why prefer f-strings over `%` formatting?**  
**A:** f-strings are faster, more readable, and support expressions inside `{}` (e.g. `f"{x * 2}"`).

**Q4: How do you check if a string is numeric?**  
**A:** `s.isdigit()` for integers only; `float(s)` in try/except for decimals; or regex for complex rules.

**Q5: What does `s[::-1]` do?**  
**A:** Reverses the string using slice step `-1`.

**Q6: Difference between `str` and `bytes`?**  
**A:** `str` is Unicode text. `bytes` is raw binary. Encode: `s.encode("utf-8")`. Decode: `b.decode("utf-8")`.

**Q7: How is a string different from a list of characters?**  
**A:** Both are sequences, but strings are immutable and hold only text; lists are mutable and can hold any types.
