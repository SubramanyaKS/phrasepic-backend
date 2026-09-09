from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_key: str
    hf_model: str
    supabase_publishable_key: str
    supabase_url: str | None = None
    allowed_origins: list[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"


settings = Settings()