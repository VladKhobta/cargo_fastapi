from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Insurance Calculator"
    port: int = 8080
    database_url: str = "postgres://root:admin@127.0.0.1:5432/database"
    imitation_api_url: str = f"http://127.0.0.1:8888"


settings = Settings()
