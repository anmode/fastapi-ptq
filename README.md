
# FastAPI: Movie Titles API

## Objective
Build a small FastAPI service that exposes a **GET** endpoint `/movies/{year}`.  
The endpoint must:
1. Accept a four‑digit `year` as a **path** parameter.
2. Fetch movie data from `https://jsonmock.hackerrank.com/api/moviesdata?Year={year}`.
3. Return a JSON payload `{"titles": [...]}` containing the **Title** of every movie in the order received.
4. If the external API returns an empty array in its `data` field, respond with HTTP **404** and body `{"detail": "No Results Found"}`.

## Tech Stack
| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.8+ | Runtime |
| FastAPI | 0.111 | Web framework |
| httpx | 0.27 | Async HTTP client |
| Uvicorn | 0.29 | ASGI server (for manual runs) |
| pytest & pytest‑asyncio | Latest | Testing |
| respx | 0.21 | Mocking external HTTP calls |

## Quick Start
```bash
# Install deps
python3 -m venv .venv    &&  source .venv/bin/activate && pip install -r requirements.txt

# Run dev server
uvicorn app.main:app --reload --port 8000
```

## Available Commands
| Command | What it does |
|---------|--------------|
| `python3 -m venv .venv    &&  source .venv/bin/activate && pip install -r requirements.txt` | install |
| `virtualenv env1 && source env1/bin/activate && pip3 install -r requirements.txt && rm -rf unit.xml && python3 manage.py test` | run tests |
| `uvicorn app.main:app --reload --port 8000` | manual run |

## Testing Criteria
Automated tests (`tests/test_main.py`) will check:
1. **200** response and correct JSON for a year with results.
2. **404** with `"No Results Found"` for a year with no movies.
3. Automatic **422** validation for non‑numeric years (FastAPI default).

