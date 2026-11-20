"""SQLAlchemy ORM models — the database tables."""
from sqlalchemy import Column, DateTime, Float, Integer, String, func

from .database import Base


class Reading(Base):
    """One telemetry reading from a sensor."""

    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(String, index=True, nullable=False)
    value = Column(Float, nullable=False)
    unit = Column(String, nullable=False, default="")
    recorded_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
