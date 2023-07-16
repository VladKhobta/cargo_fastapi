import logging.config

from fastapi import FastAPI
from fastapi import APIRouter
from tortoise.contrib.fastapi import register_tortoise

from api.insurances import rates_router
from settings import settings

# setup loggers
logging.config.fileConfig(
    "logging.conf",
    disable_existing_loggers=False,
)

# get root logger
logger = logging.getLogger(__name__)


app = FastAPI()

main_router = APIRouter()
main_router.include_router(
    rates_router,
    prefix="/rates"
)
app.include_router(main_router)

register_tortoise(
    app,
    db_url=settings.database_url,
    modules={
        "models": ["db.models"],
        "aerich.models": ["aerich.models"]
    },
    generate_schemas=True,
    add_exception_handlers=True,
)
