"""Telemetry Readings API — FastAPI + SQLAlchemy + SQLite.

Run with:
    uvicorn app.main:app --reload

Interactive docs at http://127.0.0.1:8000/docs
"""
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Telemetry Readings API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/readings", response_model=schemas.ReadingOut, status_code=201)
def create_reading(reading: schemas.ReadingCreate, db: Session = Depends(get_db)):
    db_reading = models.Reading(**reading.model_dump())
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading


@app.get("/readings", response_model=list[schemas.ReadingOut])
def list_readings(sensor_id: str | None = None, min_value: float | None = None, max_value: float | None = None, db: Session = Depends(get_db)):
    query = db.query(models.Reading)
    if sensor_id is not None:
        query = query.filter(models.Reading.sensor_id == sensor_id)
    if min_value is not None:
        query = query.filter(models.Reading.value >= min_value)
    if max_value is not None:
        query = query.filter(models.Reading.value <= max_value)
    return query.order_by(models.Reading.id).all()

#def list_readings(sensor_id: str | None = None, db: Session = Depends(get_db)):
    #query = db.query(models.Reading)
    #if sensor_id is not None:
        #query = query.filter(models.Reading.sensor_id == sensor_id)
    #return query.order_by(models.Reading.id).all()


@app.get("/readings/{reading_id}", response_model=schemas.ReadingOut)
def get_reading(reading_id: int, db: Session = Depends(get_db)):
    db_reading = db.get(models.Reading, reading_id)
    if db_reading is None:
        raise HTTPException(status_code=404, detail="Reading not found")
    return db_reading


@app.delete("/readings/{reading_id}", status_code=204)
def delete_reading(reading_id: int, db: Session = Depends(get_db)):
    db_reading = db.get(models.Reading, reading_id)
    if db_reading is None:
        raise HTTPException(status_code=404, detail="Reading not found")
    db.delete(db_reading)
    db.commit()
    return None


# --- Practice milestones (extension points) ---
# Week 2: add query filters, e.g. GET /readings?sensor_id=temp-01&min_value=20
# Week 3: add PATCH /readings/{id} for partial updates + input validation rules
# Week 4: add a summary endpoint, e.g. GET /readings/stats with per-sensor averages
