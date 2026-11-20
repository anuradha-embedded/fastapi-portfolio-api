# Practice Plan — FastAPI + Databases

**Pace:** 3 hours/day, 7 days/week (21 hrs/week), 4 weeks (~84 hours total)
**Goal:** turn the two flagged resume gaps — web frameworks and databases — into demonstrable, claimable experience.
**Project:** the Telemetry Readings API in this folder (FastAPI + SQLAlchemy + SQLite).

How to work: each day is a 3-hour block. Read the "Learn" line, then do the "Build" line. Every week ends with something working that you can demo — and the exact resume line you earn that week. Only claim a skill after you've built it.

---

## Week 1 — FastAPI fundamentals: routes, validation, your first endpoint

**Days 1–2 (6h) — Tour the scaffold.**
Learn: how FastAPI routing, path/query parameters, and Pydantic models fit together.
Build: run the API (`uvicorn app.main:app --reload`), explore the interactive docs at `/docs`, run the test suite (`pytest -q`). Read `main.py`, `schemas.py`, `models.py` until you can explain what each file does.

**Days 3–4 (6h) — Filtered listing.**
Learn: query parameters and SQLAlchemy filtering (`.filter()`, `.where()`).
Build: extend `GET /readings` with optional filters — `sensor_id`, `min_value`, `max_value`. Test each filter in `/docs`.

**Days 5–6 (6h) — Validation with teeth.**
Learn: Pydantic field validators and custom error responses (`HTTPException`).
Build: add validation rules (e.g., reject negative values for temperature sensors, require `sensor_id` to match a pattern). Return clear 422/400 errors for bad input.

**Day 7 (3h) — Test what you built.**
Learn: FastAPI's `TestClient` patterns (see `tests/test_api.py`).
Build: write tests for the filters and the validation rules — including the failure cases.

**Week 1 milestone:** a filtered, validated readings endpoint, covered by tests.
**Resume line you earn:** "Built REST API endpoints with FastAPI, including query-parameter filtering and Pydantic request validation."

---

## Week 2 — Database depth: relationships and real queries

**Days 1–2 (6h) — A second table.**
Learn: `ForeignKey`, `relationship()`, and joined loading in SQLAlchemy.
Build: add a `Sensor` model (`id`, `name`, `location`) with a one-to-many relationship to `Reading` (each reading belongs to a sensor). Create the tables and confirm the relationship works in a quick script.

**Days 3–4 (6h) — Nested responses.**
Learn: response schemas that include related objects.
Build: CRUD endpoints for sensors, plus a `GET /sensors/{id}` response that nests that sensor's readings. Decide what happens to readings when a sensor is deleted — and implement it deliberately.

**Days 5–6 (6h) — Seeding and indexing.**
Learn: why databases need seed data and indexes; the idea behind migrations.
Build: write a small seed script that populates sensors + readings with realistic data. Add indexes on the columns you filter by most (`sensor_id`, `recorded_at`) and observe the difference on larger datasets.

**Day 7 (3h) — Test the data layer.**
Learn: testing relationship behavior (cascades, nested output).
Build: tests for sensor CRUD, nested responses, and the delete behavior you chose.

**Week 2 milestone:** a two-table relational model with joined queries and seeded data.
**Resume line you earn:** "Designed relational data models with SQLAlchemy — one-to-many relationships, indexed queries, and seed/migration scripting."

---

## Week 3 — API maturity: updates, pagination, errors

**Days 1–2 (6h) — Partial updates.**
Learn: PATCH semantics and partial Pydantic models (`exclude_unset`).
Build: `PATCH /readings/{id}` — update any subset of fields, validate the result, return 404 for missing ids.

**Days 3–4 (6h) — Pagination and error standards.**
Learn: limit/offset pagination patterns and FastAPI exception handlers.
Build: paginate `GET /readings` and `GET /sensors` (`limit`, `offset`, plus a total count in the response). Standardize every error response to the same `{detail}` shape.

**Days 5–6 (6h) — Go deeper on one advanced feature.**
Learn (pick one): `BackgroundTasks` (e.g., log every write to a file asynchronously) or middleware (e.g., request timing/logging).
Build: implement your pick and prove it works with a test or a log file.

**Day 7 (3h) — Test the new surface.**
Build: tests for PATCH behavior, pagination edges (empty page, beyond-the-end), and your advanced feature.

**Week 3 milestone:** production-style API features — the kind reviewers look for.
**Resume line you earn:** "Implemented paginated list endpoints, partial updates, and standardized error handling in a FastAPI service."

---

## Week 4 — Testing, analytics, and ship-ready polish

**Days 1–3 (9h) — Harden the test suite.**
Learn: pytest fixtures and testing failure paths, not just happy paths.
Build: cover every endpoint including edge cases — invalid input, missing resources, empty filters, pagination boundaries. Aim for every route tested.

**Days 4–5 (6h) — Analytics endpoint.**
Learn: SQLAlchemy aggregate functions (`func.count`, `func.avg`, `func.min`, `func.max`, `group_by`).
Build: `GET /readings/stats` returning per-sensor aggregates — reading count, average, min, max. This is the "data engineering flavor" piece.

**Day 6 (3h) — Polish.**
Build: clean up the README (setup, endpoints, examples), add docstrings, remove dead code. The project should be presentable to a stranger.

**Day 7 (3h) — Demo day.**
Build: fresh database, run the full suite, walk through every endpoint in `/docs`, and record a 2-minute screen demo if you like. Then update your resume with the four earned lines.

**Week 4 milestone:** a tested, documented, portfolio-ready API.
**Resume line you earn:** "Built and tested a database-backed REST API (FastAPI + SQLAlchemy + SQLite) with aggregate analytics endpoints and full test coverage."

---

## After the 4 weeks — what you can claim (and only this)

- FastAPI routing, query/path parameters, and dependency injection (`Depends`)
- Pydantic request/response validation, including custom validators
- SQLAlchemy ORM: models, relationships, filtered/joined/aggregate queries, indexing
- REST API design: CRUD, PATCH partial updates, pagination, standardized errors
- API testing with pytest and FastAPI's TestClient
- SQLite-backed persistence with seed and migration scripting

What this does **not** yet make claimable: Django/Flask (different frameworks), PostgreSQL/MySQL/MongoDB (different databases), Docker/Kubernetes, CI/CD pipelines, or cloud deployment. Those are honest next steps, not today's claims. If a posting asks for them, say "SQLite/SQLAlchemy, ramping on PostgreSQL" — true and credible.
