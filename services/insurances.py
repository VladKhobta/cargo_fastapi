import datetime
import logging
from typing import Union
import httpx

from schemas.insurances import OutInsurance
from db.models import Insurance
from settings import settings


logger = logging.getLogger(__name__)


async def get_actual_rate(
        cargo_type: str,
        date: datetime.date
) -> Union[str, None]:
    logger.info("Requesting actual rate")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.imitation_api_url}/rate/?date={date}&cargo_type={cargo_type}"
            )
    except httpx.ConnectError:
        # Handling external rate api connection error
        return None

    # parsing json-response
    data = response.json()
    if str(date) not in data:
        return None

    date_rate_objects = data[str(date)]
    rate = None
    for rate_object in date_rate_objects:
        if rate_object["cargo_type"] == cargo_type:
            rate = float(rate_object["rate"])

    return rate


class InsuranceService:
    model = Insurance

    async def calculate_insurance(
            self,
            date: datetime.date,
            cargo_type: str,
            declared_value: float
    ):
        # getting actual rate
        rate = await get_actual_rate(
            cargo_type=cargo_type,
            date=date
        )

        if not rate:
            return None

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
