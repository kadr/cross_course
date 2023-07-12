from __future__ import annotations

import os
from typing import Union

from src.services.xe_currency.api import get_currencies, XEConnectionError, XEDataError

Currency = list[dict[str, Union[str, list[dict[str, Union[str, bool]]]]]]


class TestXEApi:
    """Тест для проверки метода получения данных из api XE"""

    async def test_get_xe_currency(self):
        currencies: list[Currency] = await get_currencies(os.getenv('XE_API_ID'), os.getenv('XE_API_KEY'))
        assert not isinstance(currencies, (XEConnectionError, XEDataError))
        assert len(currencies) > 0
