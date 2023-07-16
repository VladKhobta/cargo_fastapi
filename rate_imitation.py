# Rate service API imitation app

import datetime
import random
from typing import List

from fastapi import FastAPI
from fastapi import APIRouter
from pydantic import BaseModel


# Sample cargo types list for imitating real rate api response
CARGO_TYPES = [
    "Glass", "Other", "Animals", "Liquids", "Electronics"
]


class GetRate(BaseModel):
    date: datetime.date
    cargo_type: str


# Random response data generating function
def get_random_rate():
    return str(round(random.uniform(0, 0.20), 2))


def generate_random_rate_dict(
        types_set: List[str],
        origin_type: str
):
    if origin_type in types_set:
        types_set.remove(origin_type)
    return {
        "cargo_type": random.choice(types_set),
        "rate": get_random_rate()
    }


def generate_random_rate_data(
        origin_cargo_type: str,
        origin_date: datetime.date,
):
    # generating two additional dates
    random_delta_days = random.randint(1, 10)
    date1 = origin_date + datetime.timedelta(days=random_delta_days)
    date2 = origin_date - datetime.timedelta(days=random_delta_days)

    # generating response with one origin date and two random others
    return {
        origin_date: [
            {
                "cargo_type": origin_cargo_type,
                "rate": get_random_rate()
            },
            generate_random_rate_dict(CARGO_TYPES, origin_cargo_type)
        ],
        date1: [
            generate_random_rate_dict(CARGO_TYPES, origin_cargo_type),
            generate_random_rate_dict(CARGO_TYPES, origin_cargo_type)
        ],
        date2: [
            generate_random_rate_dict(CARGO_TYPES, origin_cargo_type),
            generate_random_rate_dict(CARGO_TYPES, origin_cargo_type)
        ]
    }


# Rate service imitation app and router defining
main_router = APIRouter()


@main_router.get("/")
def get_actual_rate(
        date: datetime.date,
        cargo_type: str,
):
    return generate_random_rate_data(
        cargo_type,
        date
    )


app = FastAPI(
    title="Rate Service Imitation"
)
app.include_router(
    main_router,
    prefix="/rate",
    tags=["rates"]
)
