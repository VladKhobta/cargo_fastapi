from schemas.insurances import InsuranceCalculation
from db.dals.insurances import InsuranceDAL
from db.models import Insurance

class InsuranceService:
    model = Insurance

    def __init__(self):
        pass

    async def calculate_insurance(
            self,
            body: InsuranceCalculation
    ):
        # getting actual rate
        rate = 0.02


