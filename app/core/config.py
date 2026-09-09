from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_key: str
    hf_model: str
    supabase_publishable_key: str
    supabase_url: str | None = None
    allowed_origins: list[str] = ["https://phrasepic.onrender.com"]

    class Config:
        env_file = ".env",
        env_file_encoding="utf-8",
        extra="ignore",


settings = Settings()