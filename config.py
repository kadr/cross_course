import os
from typing import Final
from dotenv import load_dotenv

from pkg.logger.iLogger import ILogger
from pkg.logger.logger import Logger

logger: ILogger = Logger()
load_dotenv()


XE_API_KEY: Final = os.getenv('XE_API_KEY')
if not XE_API_KEY:
    logger.error("не задана api ключ для XE")
    exit(1)
XE_API_ID: Final = os.getenv('XE_API_ID')
if not XE_API_ID:
    logger.error("не задана api id для XE")
    exit(1)
PGSQL_DB: Final = os.getenv('PGSQL_DB')
if not PGSQL_DB:
    logger.error("не задано имя базы БД")
    exit(1)
PGSQL_USER: Final = os.getenv('PGSQL_USER')
if not PGSQL_USER:
    logger.error("не задан имя пользователя БД")
    exit(1)
PGSQL_PASSWORD: Final = os.getenv('PGSQL_PASSWORD')
if not PGSQL_PASSWORD:
    logger.error("не задан пароль пользователя БД")
    exit(1)
PGSQL_HOST: Final = os.getenv('PGSQL_HOST')
if not PGSQL_HOST:
    logger.error("не задан хост для подключения к БД")
    exit(1)
RPC_PORT: Final = os.getenv('RPC_PORT')
