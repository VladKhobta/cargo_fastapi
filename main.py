from fastapi import FastAPI
from fastapi import APIRouter
from api.insurances import rates_router
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

main_router = APIRouter()
main_router.include_router(
    rates_router,
    prefix="/rates"
)

app.include_router(main_router)


register_tortoise(
    app,
    db_url="pg+async://fkjaks/kfsj",
    modules={
        "models": ["db.models"],
        "aerich.models": ["db.models"]
    },
    generate_schemas=True,
    add_exception_handlers=True
)
