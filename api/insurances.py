import datetime
import logging

from fastapi import APIRouter, Depends, HTTPException

from schemas.insurances import OutInsurance
from services.insurances import InsuranceService
from services.rates import get_actual_rate

logger = logging.getLogger(__name__)

rates_router = APIRouter()


@rates_router.get("/")
async def calculate_insurance(
        cargo_type: str,
        declared_value: float,
        date: datetime.date = datetime.date(2020, 6, 6),
        insurance_service: InsuranceService = Depends()
) -> OutInsurance:
    logger.info("Handling insurance calculating request")

    # getting actual rate from external api
    rate = await get_actual_rate(
        cargo_type=cargo_type,
        date=date
    )

    if not rate:
        error_message = "External rate info service is not responding"
        logger.error(error_message)
        raise HTTPException(
            status_code=504,
            detail=error_message
        )

    insurance = await insurance_service.calculate_insurance(
        rate=rate,
        date=date,
        cargo_type=cargo_type,
        declared_value=declared_value
    )
    if not insurance:
        error_message = "Rate with specified cargo_type and date not found"
        logger.error(error_message)
        raise HTTPException(
            status_code=404,
            detail=error_message
        )
    return insurance
