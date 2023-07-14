from __future__ import annotations

import os
from typing import Union

import pytest

from pkg.logger.iLogger import ILogger
from pkg.logger.logger import Logger
from services.xe_currency.const import Course
from services.xe_currency.currency import XECurrency, XEConnectionError, XEDataError

Currency = dict[str, Union[str, bool]]
logger: ILogger = Logger()


class TestXEApi:
    """Тест для проверки метода получения данных из api XE"""

    currencies: list[Currency]
    courses: list[Course]

    @pytest.mark.dependency(name='get')
    async def test_get_currencies(self):
        api_id, api_key = os.getenv('XE_API_ID'), os.getenv('XE_API_KEY')
        xe_currency: XECurrency = XECurrency(api_id, api_key, logger)
        currencies: list[Currency] = await xe_currency.get_currencies()
        assert not isinstance(currencies, (XEConnectionError, XEDataError))
        assert len(currencies) > 0
        pytest.currencies = currencies

    @pytest.mark.dependency(depends=['get'])
    async def test_save_currencies(self):
        api_id, api_key = os.getenv('XE_API_ID'), os.getenv('XE_API_KEY')
        xe_currency: XECurrency = XECurrency(api_id, api_key, logger)
        assert await xe_currency.save(pytest.currencies)

    @pytest.mark.dependency(name='calc', depends=['get'])
    async def test_calc_course(self):
        api_id, api_key = os.getenv('XE_API_ID'), os.getenv('XE_API_KEY')
        xe_currency: XECurrency = XECurrency(api_id, api_key, logger)
        courses: list = await xe_currency.get_cross_courses(pytest.currencies)
        assert not isinstance(courses, (XEConnectionError, XEDataError))
        assert len(courses) > 0
        pytest.courses = courses

    @pytest.mark.dependency(depends=['calc'])
    async def test_save_course(self):
        api_id, api_key = os.getenv('XE_API_ID'), os.getenv('XE_API_KEY')
        xe_currency: XECurrency = XECurrency(api_id, api_key, logger)
        is_save: bool = await xe_currency.save_course(pytest.courses)
        assert is_save
