from __future__ import annotations

from http import HTTPStatus
from typing import Union

import aiohttp as aiohttp
from aiohttp import BasicAuth

from constants import HOST_XE

Currency = list[dict[str, Union[str, list[dict[str, Union[str, bool]]]]]]


async def get_currencies(api_id, api_key) -> list[Currency]:
    if not api_id:
        raise AttributeError('Не задан ключ')
    if not api_key:
        raise AttributeError('Не задан идентификатор')

    url: str = f'{HOST_XE}/v1/currencies'
    currencies: list[Currency] = []
    async with aiohttp.ClientSession() as session:
        async with session.get(url, auth=BasicAuth(api_id, api_key)) as resp:
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


class XEConnectionError(Exception): ...


class XEDataError(Exception): ...
