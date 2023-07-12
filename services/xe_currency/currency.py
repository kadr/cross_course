from __future__ import annotations

import abc
from http import HTTPStatus

import aiohttp as aiohttp
from aiohttp import BasicAuth

from constants import HOST_XE
from services.xe_currency.const import Currency


class IRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, data: Currency | list[Currency]) -> bool: ...


class XECurrency:
    repository: IRepository
    api_id: str
    api_key: str

    def __init__(self, repository: IRepository, api_id: str, api_key: str):
        self.repository = repository
        if not api_id:
            raise AttributeError('Не задан ключ')
        if not api_key:
            raise AttributeError('Не задан идентификатор')
        self.api_id, self.api_key = api_id, api_key

    async def get_currencies(self) -> list[Currency]:
        url: str = f'{HOST_XE}/v1/currencies'
        currencies: list[Currency] = []
        async with aiohttp.ClientSession() as session:
            async with session.get(url, auth=BasicAuth(self.api_id, self.api_key)) as resp:
                if not resp.ok:
                    match resp.status:
                        case HTTPStatus.UNAUTHORIZED:
                            raise XEConnectionError('Не авторизован.')
                        case HTTPStatus.NOT_FOUND:
                            raise XEConnectionError(f'{url} не найден.')
                        case HTTPStatus.INTERNAL_SERVER_ERROR:
                            raise XEConnectionError('внутрення ошибка сервиса.')
                        case _:
                            raise XEConnectionError('какая то ошибка')
                result: dict[str, str | list[Currency]] = await resp.json()
                if not result:
                    raise XEDataError('вернулся пустой ответ')

                currencies = result.get('currencies')

        return currencies

    async def save(self, currencies: list[Currency]) -> bool:
        if self.repository.create(currencies):
            return True
        return False


class XEConnectionError(Exception): ...


class XEDataError(Exception): ...
