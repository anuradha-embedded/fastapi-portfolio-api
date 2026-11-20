# Telemetry Readings API

A small portfolio project: a database-backed REST API built with **FastAPI**,
**SQLAlchemy**, and **SQLite** — aimed at the web-framework and database skills
on the Python resume.

## Setup

```bash
cd fastapi-portfolio-api
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Run the API

```bash
.venv/bin/uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000/docs for the interactive API docs.

## Try it

```bash
curl -X POST http://127.0.0.1:8000/readings \
  -H "Content-Type: application/json" \
  -d '{"sensor_id": "temp-01", "value": 21.5, "unit": "C"}'

curl http://127.0.0.1:8000/readings
```

## Run the tests

```bash
.venv/bin/python -m pytest -q
```

## What's inside

- `app/main.py` — FastAPI routes (create, list, get, delete readings)
- `app/models.py` — SQLAlchemy ORM model (the `readings` table)
- `app/schemas.py` — Pydantic request/response validation
- `app/database.py` — SQLite engine + session handling
- `tests/test_api.py` — API tests with FastAPI's TestClient

Extension points for the practice plan are marked in `app/main.py`.
