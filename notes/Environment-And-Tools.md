# Environment & Developer Tools

> Additional topic — professional Python workflow  
> venv, pip, Git basics, testing, code quality.

---

## 1. Virtual Environment

Isolates project dependencies from system Python.

```bash
# Create
python -m venv venv

# Activate — Windows PowerShell
.\venv\Scripts\Activate.ps1

# Activate — Windows CMD
venv\Scripts\activate.bat

# Deactivate
deactivate
```

After activation, `pip install` affects only this project.

---

## 2. `requirements.txt`

```bash
pip install requests pandas
pip freeze > requirements.txt
pip install -r requirements.txt
```

Pin versions for reproducibility:

```text
requests==2.31.0
pandas>=2.0.0
```

Modern alternative: `pyproject.toml` with tools like Poetry or uv.

---

## 3. Project Layout (recommended)

```text
my-app/
  venv/
  src/
    my_app/
      __init__.py
      main.py
  tests/
    test_main.py
  .gitignore
  requirements.txt
  README.md
```

`.gitignore` essentials:

```text
venv/
__pycache__/
*.pyc
.env
.DS_Store
```

---

## 4. Git Essentials (for your journey)

```bash
git init
git add .
git commit -m "Add notes and exercises"
git branch -M main
git remote add origin <url>
git push -u origin main
```

| Command | Purpose |
|---------|---------|
| `git status` | See changes |
| `git diff` | See line changes |
| `git log --oneline` | History |
| `git branch feature-x` | New branch |
| `git checkout -b feature-x` | Create + switch |

---

## 5. Running Python

```bash
python script.py
python -m mypackage.main    # run as module
python -i script.py           # run then interactive shell
```

---

## 6. Testing with `pytest`

```bash
pip install pytest
```

```python
# test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0
```

```bash
pytest
pytest -v
pytest test_math.py::test_add
```

---

## 7. Code Quality Tools

| Tool | Purpose |
|------|---------|
| `black` | Auto-format code |
| `ruff` / `flake8` | Lint style/errors |
| `mypy` | Static type checking |
| `pylint` | Broader analysis |

```bash
pip install black ruff mypy
black .
ruff check .
mypy src/
```

---

## 8. Debugging Tips

```python
# Print debugging
print(f"debug: {variable=}")   # Python 3.8+ debug f-string

# Breakpoint (Python 3.7+)
breakpoint()   # drops into pdb debugger

# Logging (better than print in production)
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Server started")
```

---

## 9. PEP 8 Style (quick rules)

- 4 spaces per indent (no tabs)
- Max ~79–88 chars per line
- `snake_case` for functions/variables
- `PascalCase` for classes
- `UPPER_CASE` for constants
- Two blank lines between top-level functions/classes

---

## Interview Q&A — Tools

**Q1: Why use virtual environments?**  
**A:** Isolate dependencies per project — avoid version conflicts between projects and keep system Python clean.

**Q2: `pip` vs `conda`?**  
**A:** `pip` installs Python packages from PyPI. `conda` manages packages + environments including non-Python binaries — popular in data science.

**Q3: What is `pytest` fixture?**  
**A:** Reusable setup/teardown for tests — `@pytest.fixture` provides shared test data or connections.

**Q4: Difference between `python script.py` and `python -m package`?**  
**A:** `-m` runs a module inside a package with correct import paths relative to project root.

**Q5: What should never go in Git?**  
**A:** Secrets (`.env`, API keys), `venv/`, `__pycache__/`, large data files — use `.gitignore`.
