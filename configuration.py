from pydantic import BaseSettings


class Setting(BaseSettings):
    databaseusername: str
    databasepassword: str
    host: str
    database: str
    secretkey: str
    algorithm: str
    expirehours: int

    class Config:
        env_file = ".env"


settings = Setting()
