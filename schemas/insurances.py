import datetime

from db.models import Insurance
from tortoise.contrib.pydantic.base import PydanticModel
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel


class InsuranceCalculation(BaseModel):
    date: datetime.date
    cargo_type: str
    declared_value: float
