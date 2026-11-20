"""Pydantic schemas — request/response validation for the API."""
from datetime import datetime

#from pydantic import BaseModel, ConfigDict
from pydantic import BaseModel, ConfigDict, Field


#class ReadingCreate(BaseModel):
    #sensor_id: str
    #value: float
    #unit: str = ""

class ReadingCreate(BaseModel):
    sensor_id: str = Field(min_length=3, max_length=20, pattern=r"^[a-z0-9]+(-[a-z0-9]+)*$")
    value: float
    unit: str = ""


class ReadingOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    sensor_id: str
    value: float
    unit: str
    recorded_at: datetime
