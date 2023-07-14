from fastapi import APIRouter, Depends
from schemas.insurances import InsuranceCalculation  #, CalculatedInsurance
from services.insurances import InsuranceService

rates_router = APIRouter()


@rates_router.get("/")
async def calculate_insurance(
        body: InsuranceCalculation,
        insurance_service: InsuranceService = Depends()
) -> CalculatedInsurance:
    return await insurance_service.calculate_insurance(body)

