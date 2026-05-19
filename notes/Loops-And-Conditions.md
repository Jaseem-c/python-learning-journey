# Loops & Conditions

> Notes from: `exercises/loops & conditions/`  
> Control program flow with decisions and repetition.

---

## 1. Conditional Statements

```python
age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")

# Truthy values: non-zero numbers, non-empty collections, True
is_logged_in = True
if is_logged_in:
    print("Welcome back!")
```

### if / elif / else

```python
a = 10
if a > 5:
    print("greater")
elif a == 5:
    print("equal")
else:
    print("less")
```

### Shorthand (ternary-style)

```python
if a > 5: print("greater")

print("yes") if a > 5 else print("no")
```

### `pass` — placeholder (do nothing)

```python
if a > 5:
    pass   # avoids syntax error when block is empty
```

---

## 2. Comparison & Logical Operators

| Type | Operators |
|------|-----------|
| Comparison | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| Logical | `and`, `or`, `not` |
| Membership | `in`, `not in` |

---

## 3. `while` Loop

Runs while condition is **True**.

```python
i = 1
while i < 6:
    print(i)
    i += 1
```

**Watch out:** Forgetting to update the counter → infinite loop.

---

## 4. `for` Loop

Iterates over any **iterable** (list, string, tuple, dict keys, etc.).

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
```

Common patterns:

```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2): # 2, 4, 6, 8 (start, stop, step)
    print(i)
```

### Loop control

| Keyword | Effect |
|---------|--------|
| `break` | Exit loop immediately |
| `continue` | Skip rest of iteration, go to next |
| `else` (on loop) | Runs if loop finished without `break` |

---

## 5. `match` — Structural Pattern Matching (Python 3.10+)

Like a switch statement.

```python
day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
  # ...
    case 7:
        print("Sunday")
    case _:          # default (wildcard)
        print("Invalid day")
```

---

## Additional Notes (Beyond Basics)

### `enumerate`, `zip`, `reversed`

```python
fruits = ["apple", "banana"]
for i, fruit in enumerate(fruits):
    print(i, fruit)

names = ["Ali", "Sara"]
ages = [20, 22]
for name, age in zip(names, ages):
    print(name, age)

for x in reversed(fruits):
    print(x)
```

### `range` details

```python
range(5)        # 0, 1, 2, 3, 4
range(2, 10)    # 2 .. 9
range(0, 10, 2) # 0, 2, 4, 6, 8
list(range(3))  # [0, 1, 2]
```

### Nested loops & early exit

```python
for row in matrix:
    for cell in row:
        if cell == target:
            break      # exits inner loop only
```

Use a flag or function + `return` to break out of multiple nested loops cleanly.

### `match` with patterns (advanced)

```python
def handle(command):
    match command.split():
        case ["quit"]:
            return "bye"
        case ["add", a, b]:
            return int(a) + int(b)
        case ["greet", name]:
            return f"Hello {name}"
        case _:
            return "unknown"
```

### List comprehensions in loops (preview)

```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

Often replaces `for` + `append` — faster and more readable.

---

## Quick Reference

| Need | Use |
|------|-----|
| Repeat N times | `for i in range(N)` |
| Repeat until condition | `while condition` |
| Multi-way branch | `if/elif/else` or `match` |
| Index + value | `enumerate(items)` |
| Two lists together | `zip(a, b)` |
| Empty block | `pass` |

---

## Interview Q&A — Loops & Conditions

**Q1: `while` vs `for` — when to use which?**  
**A:** Use `for` when you know the iterable or fixed count. Use `while` when repetition depends on a condition that may change unpredictably (e.g. read until EOF, game loop).

**Q2: What is the `else` clause on a `for` loop?**  
**A:** `else` runs when the loop completes normally (no `break`). If `break` fires, `else` is skipped.

**Q3: Difference between `break` and `continue`?**  
**A:** `break` exits the loop entirely. `continue` skips to the next iteration.

**Q4: What values are falsy in Python?**  
**A:** `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `()`, `set()`, and custom objects with `__bool__` or `__len__` returning false/zero.

**Q5: What does `match` do that `if/elif` cannot easily do?**  
**A:** Pattern matching — destructure sequences, match types, capture parts of data (e.g. `case [x, y]:`).

**Q6: How do you loop with index and value?**  
**A:** `for i, val in enumerate(items):`

**Q7: Can you use `else` with `while`?**  
**A:** Yes. Same rule as `for`: `else` runs if the loop ends without `break`.
