from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    HOST: str
    PORT: int

    DATABASE_URL: str
    DIRECT_URL: str

    SUPABASE_URL: str
    SUPABASE_ANON_KEY: str

    DATABASE_ECHO: bool
    DATABASE_POOL_SIZE: int

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()