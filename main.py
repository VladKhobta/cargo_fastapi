from fastapi import FastAPI
from fastapi import APIRouter
from api.rates import rates_router

app = FastAPI()

main_router = APIRouter()
main_router.include_router(
    rates_router,
    prefix="/rates"
)

app.include_router(main_router)
