from fastapi import APIRouter, Depends
from sqlalchemy import select, desc, Result
from sqlalchemy.ext.asyncio import AsyncSession

from pkg.logger.iLogger import ILogger
from pkg.logger.logger import Logger
from src.currency.models import Currency as CurrencyModel, CrossCourse
from src.currency.schemas import Currency as CurrencySchema, GetCurrency, GetCrossCourse, CreateCrossCourse
from src.database import get_async_session

logger: ILogger = Logger()

router = APIRouter(
    prefix='/currencies',
    tags=['Currencies']
)


@router.get('/{name}', response_model=GetCurrency)
async def get_currency_by_iso(name: str, session: AsyncSession = Depends(get_async_session)):
    query = select(CurrencyModel).filter(CurrencyModel.iso == name).order_by(desc(CurrencyModel.id))
    res = (await session.execute(query)).first()
    if not res:
        raise RecordNotFoundError("Записи не найдены")
    return res[0]


@router.get('/', response_model=list[GetCurrency])
async def get_all(session: AsyncSession = Depends(get_async_session)):
    query = select(CurrencyModel).order_by(desc(CurrencyModel.id))
    result: Result = await session.execute(query)
    if result is None:
        raise RecordNotFoundError("Записи не найдены")
    return [c[0] for c in result.all()]


@router.post('/', response_model=GetCurrency)
async def add_currency(currency: CurrencySchema, session: AsyncSession = Depends(get_async_session)):
    db_currency = CurrencyModel(**currency.dict())
    logger.debug(db_currency)
    session.add(db_currency)
    await session.commit()
    await session.refresh(db_currency)
    return db_currency


router_cross_course = APIRouter(
    prefix='/courses',
    tags=['Cross Course']
)


@router_cross_course.get('/{first_currency}/{second_currency}', response_model=GetCrossCourse)
async def get_last_cross_course(first_currency: str, second_currency: str,  session: AsyncSession = Depends(get_async_session)):
    query = select(CrossCourse).filter(CrossCourse.name == f'{first_currency}/{second_currency}').order_by(desc(CrossCourse.create_at))
    res = (await session.execute(query)).first()
    if not res:
        raise RecordNotFoundError("Записи не найдены")
    return res[0]


@router_cross_course.post('/', response_model=GetCrossCourse)
async def add_cross_course(cross_course: CreateCrossCourse, session: AsyncSession = Depends(get_async_session)):
    db_cross_course = CrossCourse(**cross_course.dict())
    session.add(db_cross_course)
    await session.commit()
    await session.refresh(db_cross_course)
    return db_cross_course


class RecordNotFoundError(Exception): ...
