import datetime
import logging

from fastapi import APIRouter, Depends, HTTPException

from schemas.insurances import OutInsurance
from services.insurances import InsuranceService


logger = logging.getLogger(__name__)

rates_router = APIRouter()


@rates_router.get("/")
async def calculate_insurance(
        date: datetime.date,
        cargo_type: str,
        declared_value: float,
        insurance_service: InsuranceService = Depends()
) -> OutInsurance:
    logger.info("Handling insurance calculating request")
    insurance = await insurance_service.calculate_insurance(
        date=date,
        cargo_type=cargo_type,
        declared_value=declared_value
    )
    if not insurance:
        error_message = "Rate with specified cargo_type and date not found " \
                        "or external rate info service is not responding"
        logger.error(error_message)
        raise HTTPException(
            status_code=404,
            detail=error_message
        )
    return insurance
