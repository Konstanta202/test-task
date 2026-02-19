from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    VERSION: str = "1.0.0"

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_PORT_LOCAL: str

    ACCESS_TOKEN_EXPIRE: int
    SECRET_KEY: str
    ALGORITHM: str

    @property
    def DATABASE_URL_asyncpg(self):
        base_url = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@"
        host_port = f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return base_url + host_port

    @property
    def MIGRATION_DATABASE_URL_asyncpg(self):
        base_url = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@"
        host_port = f"{"localhost"}:{self.DB_PORT_LOCAL}/{self.DB_NAME}"
        return base_url + host_port

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )


settings = Settings()
