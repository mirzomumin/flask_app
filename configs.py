from dotenv import load_dotenv
from os import getenv

load_dotenv()


class Settings:
    HOST: str = getenv('HOST')
    PORT: int = int(getenv('PORT'))
    REDIS_HOST:str = getenv('REDIS_HOST')
    REDIS_PORT:int = int(getenv('REDIS_PORT'))


settings = Settings()
