# Error Handling

> Additional topic — not yet in `exercises/`  
> Handle failures gracefully instead of crashing.

---

## 1. Exceptions Basics

When something goes wrong, Python raises an **exception**. If uncaught, the program stops with a traceback.

```python
10 / 0          # ZeroDivisionError
int("abc")      # ValueError
d = {}
d["key"]        # KeyError
```

Common built-in exceptions:

| Exception | When |
|-----------|------|
| `ValueError` | Wrong value, right type |
| `TypeError` | Wrong type for operation |
| `KeyError` | Missing dict key |
| `IndexError` | List index out of range |
| `FileNotFoundError` | File missing |
| `AttributeError` | Attribute does not exist |

---

## 2. try / except / else / finally

```python
try:
    age = int(input("Age: "))
    result = 100 / age
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("Age cannot be zero")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print(f"Result: {result}")   # runs only if no exception
finally:
    print("Cleanup always runs")
```

| Block | Purpose |
|-------|---------|
| `try` | Code that might fail |
| `except` | Handle specific errors |
| `else` | Runs if **no** exception |
| `finally` | Always runs (cleanup) |

---

## 3. Raising Exceptions

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount
```

### Custom exception class

```python
class InvalidEmailError(Exception):
  pass

def register(email):
    if "@" not in email:
        raise InvalidEmailError(f"Invalid email: {email}")
```

---

## 4. `assert` — debugging checks

```python
def divide(a, b):
    assert b != 0, "b must not be zero"
    return a / b
```

Use `assert` for programmer errors in development — not for user input validation (use `raise`).

---

## 5. Best Practices

- Catch **specific** exceptions, not bare `except:`.
- Do not silence errors with empty `except: pass`.
- Log or re-raise when you cannot handle meaningfully.
- Use `get()` on dicts to avoid `KeyError` when appropriate.

```python
# EAFP — Easier to Ask Forgiveness than Permission (Pythonic)
try:
    value = my_dict[key]
except KeyError:
    value = default
```

---

## Interview Q&A — Error Handling

**Q1: Difference between `except Exception` and bare `except`?**  
**A:** `except Exception` catches most errors but not `KeyboardInterrupt` / `SystemExit`. Bare `except:` catches everything including those — avoid it.

**Q2: What is the purpose of `finally`?**  
**A:** Guaranteed cleanup — close files, release connections — whether or not an exception occurred.

**Q3: When to use `raise` vs `return` an error?**  
**A:** Use `raise` for exceptional conditions that break normal flow. Return error codes/objects only when your API design prefers explicit error values.

**Q4: What is exception chaining?**  
**A:** `raise NewError("msg") from original_error` preserves the original traceback for debugging.

**Q5: EAFP vs LBYL?**  
**A:** EAFP = try/except (Pythonic). LBYL = Look Before You Leap (check `if key in d` first). EAFP is often cleaner when failure is uncommon.
