from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Insurance Calculator"
    port: int = 8080
    database_url: str = "postgres://root:admin@host.docker.internal:5432/postgres"
    imitation_api_url: str = f"http://127.0.0.1:8888"


settings = Settings()
