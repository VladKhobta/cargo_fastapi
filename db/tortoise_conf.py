from settings import settings

TORTOISE_ORM = {
    "connections": {
        "default": settings.database_url
    },
    "apps": {
        "models": {
            "models": [
                "db.models",
                "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}
