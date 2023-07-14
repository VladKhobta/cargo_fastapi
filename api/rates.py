from fastapi import APIRouter
from schemas.rates import CreateRates

rates_router = APIRouter()


@rates_router.post("/")
def create_rates(
        body: CreateRates
):
    return None
