from pydantic import BaseModel


class OutInsurance(BaseModel):
    insurance: float
