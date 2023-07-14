import datetime
from typing import Dict, List
from pydantic import BaseModel


class InsuranceCalculation(BaseModel):
    cargo_type: str
