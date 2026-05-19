# APIs & HTTP (Python)

> Additional topic — for backend & AI app goals in your README  
> Talk to web services — REST APIs, JSON, authentication basics.

---

## 1. HTTP Basics

| Method | Typical use |
|--------|-------------|
| `GET` | Read data |
| `POST` | Create / submit |
| `PUT` / `PATCH` | Update |
| `DELETE` | Remove |

Status codes:

| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 400 | Bad request |
| 401 | Unauthorized |
| 404 | Not found |
| 500 | Server error |

---

## 2. `requests` Library

```bash
pip install requests
```

```python
import requests

# GET
response = requests.get("https://api.github.com/users/octocat")
response.status_code          # 200
response.json()               # dict / list
response.text                 # raw string

# POST with JSON body
payload = {"name": "Jaseem", "role": "student"}
r = requests.post(
    "https://httpbin.org/post",
    json=payload,
    headers={"Content-Type": "application/json"},
    timeout=10,
)

# Query parameters
requests.get("https://api.example.com/search", params={"q": "python", "page": 1})
```

Always set `timeout=` to avoid hanging forever.

---

## 3. Handling API Responses Safely

```python
import requests

def fetch_user(user_id: str) -> dict:
    url = f"https://api.example.com/users/{user_id}"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()   # raises for 4xx/5xx
        return r.json()
    except requests.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.RequestException as e:
        print(f"Network error: {e}")
    return {}
```

---

## 4. API Keys & Headers

```python
headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Accept": "application/json",
}
requests.get(url, headers=headers)
```

Never commit API keys to Git — use environment variables:

```python
import os
api_key = os.environ.get("OPENAI_API_KEY")
```

---

## 5. REST API Design (concepts)

- **Resource** — noun URLs: `/users`, `/users/1`
- **Stateless** — each request has all info needed
- **JSON** — common data format
- **Versioning** — `/api/v1/users`

---

## 6. FastAPI Preview (modern Python APIs)

```python
# pip install fastapi uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "name": "Jaseem"}
```

Run: `uvicorn main:app --reload`

---

## 7. AI / LLM APIs (pattern)

Most AI APIs follow the same pattern:

```python
import os
import requests

def chat(prompt: str) -> str:
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"},
        json={
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=60,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
```

Official SDKs (`openai`, `anthropic`) wrap this — prefer SDKs in production.

---

## Interview Q&A — APIs

**Q1: REST vs SOAP?**  
**A:** REST uses HTTP + JSON/XML, stateless, flexible URLs. SOAP is XML-based, heavier, often enterprise legacy. Most modern apps use REST.

**Q2: What is `requests.raise_for_status()`?**  
**A:** Raises `HTTPError` if status is 4xx or 5xx — cleaner than manual `if response.status_code != 200`.

**Q3: GET vs POST?**  
**A:** GET retrieves data (idempotent, params in URL). POST sends data to create/process (body, not cached by browsers).

**Q4: How do you secure API keys?**  
**A:** Environment variables, `.env` files (in `.gitignore`), secret managers in cloud — never hardcode in source.

**Q5: What is rate limiting?**  
**A:** API restricts requests per time window. Handle with retries, backoff, and respect `Retry-After` headers.

**Q6: JSON vs form data?**  
**A:** JSON in body with `Content-Type: application/json`. Forms use `application/x-www-form-urlencoded` or `multipart` for files.
