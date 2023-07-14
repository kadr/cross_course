from __future__ import annotations

import abc
import asyncio
import time
from http import HTTPStatus

import aiohttp as aiohttp
import requests
from aiohttp import BasicAuth
from requests import Response

from constants import HOST_XE, APP_HOST
from pkg.logger.iLogger import ILogger
from services.xe_currency.const import Currency, Course

REPEAT_TIMEOUT: int = 3 * 60


class IRepository(abc.ABC):
    @abc.abstractmethod
    async def create(self, data: Currency | list[Currency]) -> bool: ...


class XECurrency:
    # repository: IRepository
    api_id: str
    api_key: str
    log: ILogger

    def __init__(self, api_id: str, api_key: str, log: ILogger):
        # self.repository = repository
        if not api_id:
            raise AttributeError('Не задан ключ')
        if not api_key:
            raise AttributeError('Не задан идентификатор')
        self.api_id, self.api_key = api_id, api_key
        self.log = log

    async def get_currencies(self) -> list[Currency]:
        url: str = f'{HOST_XE}/v1/currencies'
        currencies: list[Currency] = []
        try:
            async with aiohttp.ClientSession(conn_timeout=10, read_timeout=5) as session:
                self.log.info(f'отправляем запрос на {url}')
                async with session.get(url, auth=BasicAuth(self.api_id, self.api_key)) as resp:
                    if not resp.ok:
                        match resp.status:
                            case HTTPStatus.UNAUTHORIZED:
                                self.log.error(f'Не удалось авторизоваться. {await resp.text()}')
                            case HTTPStatus.NOT_FOUND:
                                self.log.error(f'Не найден адрес. {await resp.text()}')
                            case HTTPStatus.INTERNAL_SERVER_ERROR:
                                self.log.error(f'Внутренняя ошибка сервиса. {await resp.text()}')
                            case _:
                                self.log.error(await resp.text())
                        self.log.error(await resp.text())
                        self.log.info(f'Повторная отправка через {REPEAT_TIMEOUT} сек.')
                        time.sleep(REPEAT_TIMEOUT)
                        await self.get_currencies()

                    result: dict[str, str | list[Currency]] = await resp.json()
                    if not result:
                        self.log.error(f'Пустой ответ, записи не найдены.')
                    self.log.info(f'Найдено {len(currencies)} записей.')
                    currencies = result.get('currencies')
        except (asyncio.exceptions.TimeoutError, aiohttp.client_exceptions.ClientConnectionError) as err:
            self.log.error(str(err))
            self.log.info(f'Повторная отправка через {REPEAT_TIMEOUT} сек.')
            time.sleep(REPEAT_TIMEOUT)
            await self.get_currencies()

        return currencies

    async def save(self, currencies: list[Currency]) -> bool:
        self.log.info('Сохраняем записи в базу.')
        for currency in currencies[:10]:
            response: Response = requests.post(f'{APP_HOST}/currencies', json=currency)
            if not response.ok:
                return False

        return True

    async def get_cross_courses(self, currencies: list[Currency]):
        """
        1. циклом пройтись по валютам, и по каждой валюте запросить курс к доллару
        2.
        2. формула А/С = (А/В) * (В/С). A - RUB, C - TRY, B - USD: RUB/TRY = (RUB/USD) * (USD/TRY)
           RUB/TRY = (1/90,18)/(1/26.13) = 0.28975382568196933
        """
        currency_courses: list[dict[str, str | float]] = []
        i = 0
        currencies = currencies[:20]
        usd: float = await self.__get_currency_course('USD')
        while i < len(currencies):
            first_currency = currencies[i].get('iso')
            second_currency = currencies[i + 1].get('iso')
            first_course: float | None = await self.__get_currency_course(first_currency)
            second_course: float | None = await self.__get_currency_course(second_currency)
            if first_course and second_course:
                course = (usd / first_course) / (usd / second_course)
                currency_courses.append({'name': f'{first_currency}/{second_currency}', 'course': course})
            i += 2
        return currency_courses

    async def save_course(self, courses: list[dict[str, str | float]]) -> bool:
        self.log.info('Сохраняем записи в базу.')
        for course in courses:
            response: Response = requests.post(f'{APP_HOST}/courses', json=course)
            if not response.ok:
                return False

        return True

    async def __get_currency_course(self, name_to: str, name_from: str = 'USD') -> float | None:
        url: str = f'{HOST_XE}/v1/convert_from'
        async with aiohttp.ClientSession(conn_timeout=10, read_timeout=5) as session:
            self.log.info(f'отправляем запрос на {url}')
            async with session.get(url, params={'from': name_from, 'to': name_to},
                                   auth=BasicAuth(self.api_id, self.api_key)) as resp:
                if not resp.ok:
                    match resp.status:
                        case HTTPStatus.UNAUTHORIZED:
                            self.log.error(f'Не удалось авторизоваться. {await resp.text()}')
                        case HTTPStatus.NOT_FOUND:
                            self.log.error(f'Не найден адрес. {await resp.text()}')
                        case HTTPStatus.INTERNAL_SERVER_ERROR:
                            self.log.error(f'Внутренняя ошибка сервиса. {await resp.text()}')
                        case _:
                            self.log.error(await resp.text())
                result: Course = await resp.json()
                if not result:
                    self.log.error(f'Пустой ответ, записи не найдены.')

                return result.get('to')[0].get('mid')


class XEConnectionError(Exception):
    ...


class XEDataError(Exception):
    ...
