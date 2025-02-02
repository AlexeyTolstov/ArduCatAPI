from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SERVER_ADDRESS: str
    SERVER_HOST: str
    SERVER_PORT: int

    model_config = SettingsConfigDict(env_file=".env")



settings = Settings()