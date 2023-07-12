from __future__ import annotations

import os
from typing import Union

import pytest

from services.xe_currency.currency import XECurrency, XEConnectionError, XEDataError
from services.xe_currency.repository_fake import RepositoryFake

Currency = dict[str, Union[str, bool]]


class TestXEApi:
    """Тест для проверки метода получения данных из api XE"""

    currencies: list[Currency]
    @pytest.mark.dependency(name='get')
    async def test_get_currencies(self):
        api_id, api_key = os.getenv('XE_API_ID'), os.getenv('XE_API_KEY')
        repository: RepositoryFake = RepositoryFake()
        xe_currency: XECurrency = XECurrency(repository, api_id, api_key)
        currencies: list[Currency] = await xe_currency.get_currencies()
        assert not isinstance(currencies, (XEConnectionError, XEDataError))
        assert len(currencies) > 0
        pytest.currencies = currencies

    @pytest.mark.dependency(depends=['get'])
    async def test_save_currencies(self):
        api_id, api_key = os.getenv('XE_API_ID'), os.getenv('XE_API_KEY')
        repository: RepositoryFake = RepositoryFake()
        xe_currency: XECurrency = XECurrency(repository, api_id, api_key)
        assert await xe_currency.save(pytest.currencies)

