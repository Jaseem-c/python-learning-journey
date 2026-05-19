# Data Structures

> Notes from: `exercises/dataStructures/`  
> Four core collections — pick by mutability, ordering, and duplicates.

---

## Comparison Table

| Type | Ordered | Mutable | Duplicates | Indexed access |
|------|---------|---------|------------|----------------|
| **list** | Yes | Yes | Yes | Yes `[0]` |
| **tuple** | Yes | No | Yes | Yes `[0]` |
| **dict** | Yes (3.7+) | Yes | Keys: No | By key |
| **set** | No | Yes* | No | No — loop only |

\* Set elements are immutable; you add/remove items from the set.

---

## 1. Lists

```python
fruits = ["apple", "banana", "cherry"]
fruits[0]
len(fruits)
fruits[1:3] = ["blackcurrant", "watermelon"]  # slice assign
```

| Method | Action |
|--------|--------|
| `append(x)` | Add at end |
| `insert(i, x)` | Add at index |
| `extend(iterable)` | Add multiple |
| `remove(x)` | Remove first match |
| `pop(i)` | Remove & return at index |
| `clear()` | Empty list |
| `sort()` / `sort(reverse=True)` | In-place sort |
| `copy()` | Shallow copy |

```python
# Membership
if "apple" in fruits:
    print("found")

# List comprehension
newlist = [x for x in fruits if "a" in x]

# Copy (avoid aliasing bugs)
mylist = fruits.copy()
```

---

## 2. Tuples

```python
fruits = ("apple", "banana", "cherry")
fruits[0]

# Single-item tuple — trailing comma required
thistuple = ("apple",)    # tuple
not_tuple = ("apple")     # str, not tuple!
```

**Workaround to “modify”:** convert → list → tuple.

```python
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
```

```python
del thistuple   # delete entire tuple
```

Use tuples for: fixed records, dict keys, return multiple values, data that should not change.

---

## 3. Dictionaries

Key-value pairs. Keys must be **hashable** (immutable types).

```python
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["brand"]
thisdict.get("model")   # safer — returns None if missing
thisdict.keys()
thisdict.values()
thisdict.items()
```

| Operation | Code |
|-----------|------|
| Change | `d["year"] = 2020` or `d.update({"year": 2021})` |
| Add | `d["color"] = "red"` |
| Remove key | `d.pop("model")` |
| Remove last | `d.popitem()` |
| Clear | `d.clear()` |
| Delete | `del d` |

```python
# Loop
for key in thisdict:
    print(key, thisdict[key])

for k, v in thisdict.items():
    print(k, v)

if "model" in thisdict:
    print("key exists")
```

---

## 4. Sets

Unordered, **unique** elements only.

```python
thisset = {"apple", "banana", "cherry", "apple"}
# {'apple', 'banana', 'cherry'} — duplicate removed

thisset.add("orange")
thisset.update(["mango", "grapes"])
thisset.remove("banana")    # KeyError if missing
thisset.discard("banana")   # no error if missing
thisset.pop()               # removes arbitrary element
```

### Set operations

| Operation | Method | Operator |
|-----------|--------|----------|
| Union | `.union()` | `\|` |
| Intersection | `.intersection()` | `&` |
| Difference | `.difference()` | `-` |
| Symmetric diff | `.symmetric_difference()` | `^` |

```python
set3 = set1.union(set2)
set4 = set1 | set2

set3 = set1.intersection(set2)
set4 = set1 & set2

set3 = set1.difference(set2)
set4 = set1 - set2
```

Use sets for: deduplication, membership tests (fast), math-style collections.

---

## Additional Notes (Beyond Basics)

### Comprehensions (all four types)

```python
# List
squares = [x**2 for x in range(10)]

# Dict
word_len = {w: len(w) for w in ["hi", "hello"]}

# Set
unique_lens = {len(w) for w in words}

# Generator (lazy)
gen = (x**2 for x in range(10_000_000))   # memory efficient
```

### `collections` module (know these)

```python
from collections import defaultdict, Counter, deque

# Auto-create missing keys
dd = defaultdict(list)
dd["fruits"].append("apple")

# Count occurrences
Counter("banana")   # Counter({'a': 3, 'n': 2, 'b': 1, ...})

# Fast append/pop from both ends
q = deque([1, 2, 3])
q.appendleft(0)
```

### `defaultdict`, `OrderedDict` note

Regular `dict` keeps insertion order since 3.7 — `OrderedDict` only needed for special reorder ops.

### Stack & queue patterns

```python
stack = []
stack.append(1)    # push
stack.pop()        # pop

from collections import deque
queue = deque()
queue.append(1)       # enqueue
queue.popleft()       # dequeue — O(1)
```

### Nested structures

```python
users = [
    {"name": "Ali", "skills": ["Python", "SQL"]},
    {"name": "Sara", "skills": ["JS"]},
]

# Safe access
skill = users[0].get("skills", [])[0] if users else None
```

### `collections.namedtuple`

Lightweight immutable records:

```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
p.x, p.y
```

### Sorting custom objects

```python
students.sort(key=lambda s: s["marks"], reverse=True)
sorted(students, key=lambda s: (-s["marks"], s["name"]))
```

---

## Quick Reference — When to Use What

| Need | Use |
|------|-----|
| Ordered, changeable sequence | `list` |
| Fixed data, hashable keys | `tuple` |
| Label → value lookup | `dict` |
| Unique items, set math | `set` |
| Counting frequencies | `Counter` |
| Default dict values | `defaultdict` |
| Fast queue | `deque` |

---

## Interview Q&A — Data Structures

**Q1: List vs tuple — main differences?**  
**A:** Lists are mutable, slower, use `[]`. Tuples are immutable, faster, hashable (if all items hashable), use `()`. Tuples protect data; lists for dynamic collections.

**Q2: How do you merge two dictionaries (Python 3.9+)?**  
**A:** `d3 = d1 | d2` or `d1.update(d2)`. Older: `{**d1, **d2}`.

**Q3: What happens if you use a list as a dict key?**  
**A:** `TypeError` — lists are unhashable. Use tuple instead.

**Q4: `remove()` vs `pop()` vs `discard()` on sets?**  
**A:** On sets: `remove(x)` errors if missing; `discard(x)` silently does nothing; `pop()` removes arbitrary element. On lists: `remove(value)` by value; `pop(index)` by index.

**Q5: Shallow copy vs deep copy?**  
**A:** Shallow (`copy()`, `list.copy()`) copies outer container; nested objects are shared. Deep (`copy.deepcopy()`) copies nested objects too.

**Q6: Time complexity of `x in list` vs `x in set`?**  
**A:** List: O(n). Set/dict: O(1) average — prefer sets for frequent membership checks.

**Q7: What is list comprehension?**  
**A:** Concise syntax to build lists: `[expr for item in iterable if condition]`. Often faster and clearer than manual loops.

**Q8: Difference between `get()` and `[]` on dict?**  
**A:** `d["key"]` raises `KeyError` if missing. `d.get("key", default)` returns `default` (or `None`) without raising.

**Q9: Can a set contain lists?**  
**A:** No — set elements must be hashable. Lists are mutable and unhashable.

**Q10: How is dict order guaranteed?**  
**A:** From Python 3.7+, insertion order is preserved (official language guarantee in 3.7+).

**Q11: What is `Counter` used for?**  
**A:** Counting hashable items — e.g. word frequency, vote counts. Methods: `most_common(n)`, `elements()`.

**Q12: List comprehension vs generator expression?**  
**A:** List comp `[...]` builds full list in memory. Generator `(...)` yields one item at a time — better for large data.
