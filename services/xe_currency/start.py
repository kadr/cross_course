from __future__ import annotations

import os

from pkg.logger.iLogger import ILogger
from services.xe_currency.const import Currency
from services.xe_currency.currency import XECurrency

RECONNECT_TIMEOUT_SEC: int = 3 * 60
PARSE_TIMEOUT_SEC: int = 60 * 60


async def start(log: ILogger) -> None:
    log.info('Запускаем обработчик для работы с XE')
    api_id, api_key = os.getenv('XE_API_ID'), os.getenv('XE_API_KEY')
    xe_currency: XECurrency = XECurrency(api_id, api_key, log)
    currencies: list[Currency] = await xe_currency.get_currencies()
    if currencies:
        await xe_currency.save(currencies)
        courses: list[dict[str, str | float]] = await xe_currency.get_cross_courses(currencies)
        if courses:
            await xe_currency.save_course(courses)
