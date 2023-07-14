

DATABASE_URL = "pgasync+://..."

DATABASE_MODELS = [
    "db.models"
]

TORTOISE_ORM = {
    "connection": dict(DATABASE_URL),
    "apps": {
        "models": {
            "models": DATABASE_MODELS,
            "default_connection": "default",
        }
    },
    # "timezone":
}
