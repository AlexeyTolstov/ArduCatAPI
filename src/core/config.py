from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SERVER_ADDRESS: str
    SERVER_HOST: str
    SERVER_PORT: int

    MySQL_USERNAME: str
    MySQL_PASSWORD: str
    MySQL_HOST: str
    MySQL_PORT: int
    MySQL_DATABASE: str

    RANDOM_SECRET: str

    @property
    def DATABASE_URL(self) -> str:
        return f"mysql://{self.MySQL_USERNAME}:{self.MySQL_PASSWORD}@{self.MySQL_HOST}:{self.MySQL_PORT}/{self.MySQL_DATABASE}"

    @property
    def ASYNC_DATABASE_URL(self) -> str:
        return f"mysql+asyncmy://{self.MySQL_USERNAME}:{self.MySQL_PASSWORD}@{self.MySQL_HOST}:{self.MySQL_PORT}/{self.MySQL_DATABASE}"


    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )



settings = Settings()