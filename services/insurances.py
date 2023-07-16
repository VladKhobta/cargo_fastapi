import datetime
import logging

from schemas.insurances import OutInsurance
from db.models import Insurance


logger = logging.getLogger(__name__)


class InsuranceService:
    model = Insurance

    async def calculate_insurance(
            self,
            rate: float,
            date: datetime.date,
            cargo_type: str,
            declared_value: float
    ):
        # saving insurance calculation into db
        value = rate * declared_value
        new_insurance = await self.model.create(
            date=date,
            cargo_type=cargo_type,
            declared_value=declared_value,
            rate=rate,
            value=value
        )
        return OutInsurance(insurance=new_insurance.value)
