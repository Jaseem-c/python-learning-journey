# File Handling

> Additional topic — aligns with your README goals  
> Read/write data on disk — configs, logs, CSV, JSON.

---

## 1. Opening Files

```python
# Always prefer context manager (auto-closes file)
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
```

| Mode | Meaning |
|------|---------|
| `"r"` | Read (default) |
| `"w"` | Write — **overwrites** |
| `"a"` | Append |
| `"r+"` | Read and write |
| `"rb"` / `"wb"` | Binary read/write |

---

## 2. Reading Methods

```python
with open("data.txt", "r") as f:
    all_text = f.read()           # entire file as string
    lines = f.readlines()         # list of lines (with \n)
    
with open("data.txt", "r") as f:
    for line in f:                # memory-efficient for large files
        print(line.strip())
```

---

## 3. Writing

```python
lines = ["line1\n", "line2\n"]
with open("out.txt", "w") as f:
    f.writelines(lines)

with open("log.txt", "a") as f:
    f.write("new entry\n")
```

---

## 4. Paths — `pathlib` (modern, preferred)

```python
from pathlib import Path

p = Path("notes") / "Basics.md"
print(p.exists())
print(p.suffix)        # .md
print(p.read_text(encoding="utf-8"))
p.write_text("content", encoding="utf-8")

for file in Path(".").glob("**/*.py"):
    print(file)
```

---

## 5. JSON Files

```python
import json

data = {"name": "Jaseem", "skills": ["Python", "SQL"]}

with open("user.json", "w") as f:
    json.dump(data, f, indent=2)

with open("user.json", "r") as f:
    loaded = json.load(f)
```

---

## 6. CSV (tabular data)

```python
import csv

with open("scores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerow(["Ali", 90])

with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["score"])
```

---

## 7. Context Manager — why `with`?

Ensures file is closed even if an error occurs:

```python
# Avoid — easy to leak file handles
f = open("data.txt")
data = f.read()
f.close()

# Prefer
with open("data.txt") as f:
    data = f.read()
```

Custom context manager:

```python
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

with tag("h1"):
    print("Hello")
```

---

## Interview Q&A — File Handling

**Q1: Why use `with open()` instead of `open()` + `close()`?**  
**A:** `with` guarantees the file closes via context manager protocol (`__enter__` / `__exit__`), even on exceptions.

**Q2: Difference between `read()`, `readline()`, `readlines()`?**  
**A:** `read()` — whole file. `readline()` — one line. `readlines()` — all lines as list.

**Q3: How do you handle file-not-found?**  
**A:** `try/except FileNotFoundError` or check `Path.exists()` first.

**Q4: `json.load` vs `json.loads`?**  
**A:** `load` reads from file object. `loads` parses a JSON **string**.

**Q5: Why specify `encoding="utf-8"`?**  
**A:** Avoid platform-dependent defaults and encoding errors on Windows with non-ASCII text.
