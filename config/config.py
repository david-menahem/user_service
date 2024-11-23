from pydantic.v1 import BaseSettings


class Config(BaseSettings):
    MYSQL_DATABASE: str = "user_service"
    MYSQL_USER: str = "user"
    MYSQL_PASSWORD: str = "123456"
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: str = "3307"
    DATABASE_URL: str = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'
    POLL_SERVICE_BASE_URL = "http://localhost:8001"
