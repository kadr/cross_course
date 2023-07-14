from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import PGSQL_HOST, PGSQL_DB, PGSQL_USER, PGSQL_PASSWORD

DATABASE_URL = f'postgresql+asyncpg://{PGSQL_USER}:{PGSQL_PASSWORD}@{PGSQL_HOST}/{PGSQL_DB}?async_fallback=True'
Base = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(bind=engine, class_=AsyncSession, autocommit=False, autoflush=False,
                             expire_on_commit=False)


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session
