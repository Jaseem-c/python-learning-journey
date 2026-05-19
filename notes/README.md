# Python Learning Notes

Notes from your **exercises** plus **additional topics** for interviews and real projects.  
Each file has core content, **Additional Notes** (extra depth), and **Interview Q&A**.

Use these notes together with the external references below — they cover the same topics in more depth with examples and exercises.

---

## External References

### [W3Schools Python Tutorial](https://www.w3schools.com/python/)

Beginner-friendly tutorial with **Try it Yourself** examples, exercises, and quizzes.

| W3Schools section | Maps to your notes |
|-------------------|-------------------|
| [Variables](https://www.w3schools.com/python/python_variables.asp), [Data Types](https://www.w3schools.com/python/python_datatypes.asp), [Casting](https://www.w3schools.com/python/python_casting.asp) | [Basics.md](./Basics.md) |
| [Strings](https://www.w3schools.com/python/python_strings.asp) | [Strings.md](./Strings.md) |
| [If...Else](https://www.w3schools.com/python/python_conditions.asp), [Match](https://www.w3schools.com/python/python_match.asp), [While](https://www.w3schools.com/python/python_while_loop.asp), [For](https://www.w3schools.com/python/python_for_loops.asp) | [Loops-And-Conditions.md](./Loops-And-Conditions.md) |
| [Functions](https://www.w3schools.com/python/python_functions.asp), [Lambda](https://www.w3schools.com/python/python_lambda.asp), [Decorators](https://www.w3schools.com/python/python_decorators.asp), [Recursion](https://www.w3schools.com/python/python_recursion.asp) | [Functions.md](./Functions.md) |
| [Lists](https://www.w3schools.com/python/python_lists.asp), [Tuples](https://www.w3schools.com/python/python_tuples.asp), [Sets](https://www.w3schools.com/python/python_sets.asp), [Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp) | [Data-Structures.md](./Data-Structures.md) |
| [OOP](https://www.w3schools.com/python/python_classes.asp) — Classes, Inheritance, Polymorphism, Encapsulation | [Oops.md](./Oops.md) |
| [Try...Except](https://www.w3schools.com/python/python_try_except.asp) | [Error-Handling.md](./Error-Handling.md) |
| [File Handling](https://www.w3schools.com/python/python_file_handling.asp) | [File-Handling.md](./File-Handling.md) |
| [Modules](https://www.w3schools.com/python/python_modules.asp), [PIP](https://www.w3schools.com/python/python_pip.asp) | [Modules-And-Imports.md](./Modules-And-Imports.md) |
| [JSON](https://www.w3schools.com/python/python_json.asp), [RegEx](https://www.w3schools.com/python/python_regex.asp) | [File-Handling.md](./File-Handling.md), [Strings.md](./Strings.md) |
| [VirtualEnv](https://www.w3schools.com/python/python_virtualenv.asp) | [Environment-And-Tools.md](./Environment-And-Tools.md) |

**Also useful on W3Schools:** [Python Exercises](https://www.w3schools.com/python/python_exercises.asp) · [Python Quiz](https://www.w3schools.com/python/python_quiz.asp) · [Python Reference](https://www.w3schools.com/python/python_reference.asp) · [Interview Q&A](https://www.w3schools.com/python/python_interview_questions.asp)

---

### [Python Developer Roadmap — roadmap.sh](https://roadmap.sh/python)

Step-by-step path to become a **modern Python developer** (2026). Use it to plan what to learn after fundamentals.

| Roadmap focus | Your status / next step |
|---------------|-------------------------|
| Python basics — types, functions, OOP | In progress (`notes/` + `exercises/`) |
| Data structures & algorithms | Start after core Python — see roadmap DSA branch |
| Git & version control | [Environment-And-Tools.md](./Environment-And-Tools.md) |
| Virtual env, package managers | [Environment-And-Tools.md](./Environment-And-Tools.md) |
| Web backend — Django / Flask, REST APIs | [APIs-And-HTTP.md](./APIs-And-HTTP.md) → then Django/Flask on roadmap |
| Data science — NumPy, Pandas | Planned (see “Still to add later” below) |
| Testing, CI/CD, deployment | [Environment-And-Tools.md](./Environment-And-Tools.md) → expand later |
| Databases — SQL, MongoDB | Planned — W3Schools has [MySQL](https://www.w3schools.com/python/python_mysql.asp) & [MongoDB](https://www.w3schools.com/python/python_mongodb.asp) tutorials |

**Roadmap tips (from [roadmap.sh/python](https://roadmap.sh/python)):**
- Pick a direction early: **web backend**, **data science**, or **automation** — libraries differ (Django/Flask vs Pandas/TensorFlow vs scripting).
- Learn **Git**, build small **projects** (APIs, automation, data), and contribute to **open source** for portfolio experience.
- Strong **problem-solving** + **data structures** help in interviews even if not required for every app.

---

## From your exercises

| Topic | File | Exercises |
|-------|------|-----------|
| Variables, types, casting | [Basics.md](./Basics.md) | `exercises/basics/` |
| Strings | [Strings.md](./Strings.md) | `exercises/basics/strings.py` |
| if/else, loops, match | [Loops-And-Conditions.md](./Loops-And-Conditions.md) | `exercises/loops & conditions/` |
| Functions, lambda, decorators | [Functions.md](./Functions.md) | `exercises/functions/` |
| list, tuple, dict, set | [Data-Structures.md](./Data-Structures.md) | `exercises/dataStructures/` |
| OOP (4 pillars) | [Oops.md](./Oops.md) | `exercises/oops/` |

---

## Additional topics (beyond exercises)

| Topic | File | Why learn it |
|-------|------|--------------|
| try/except, custom errors | [Error-Handling.md](./Error-Handling.md) | Production-ready code |
| Files, JSON, CSV | [File-Handling.md](./File-Handling.md) | Data & configs |
| imports, packages, pip | [Modules-And-Imports.md](./Modules-And-Imports.md) | Organize real projects |
| Generators, itertools, idioms | [Advanced-Python.md](./Advanced-Python.md) | Senior-level Python |
| REST, requests, FastAPI intro | [APIs-And-HTTP.md](./APIs-And-HTTP.md) | Backend & AI apps |
| venv, pytest, Git, PEP 8 | [Environment-And-Tools.md](./Environment-And-Tools.md) | Professional workflow |

---

## How to use

1. **Learned in class/exercises** → read the matching exercise file first.
2. **Going deeper** → read **Additional Notes** sections inside each file.
3. **New topic** → open the extra files above when ready.
4. **Before interviews** → review Interview Q&A at the bottom of each file.
5. **Your own notes** → add examples at the bottom of any file as you practice.

---

## Suggested learning order (additional)

1. Error-Handling  
2. File-Handling  
3. Modules-And-Imports  
4. Environment-And-Tools  
5. Advanced-Python  
6. APIs-And-HTTP  

---

## Still to add later

- Async (`async`/`await`)
- Databases (SQLite, SQLAlchemy)
- Python for AI (NumPy, pandas, LangChain)
