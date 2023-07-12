from __future__ import annotations

import logging

from services.xe_currency.currency import IRepository
from services.xe_currency.const import Currency


class RepositoryFake(IRepository):
    db: list[Currency] = []

    def create(self, data: Currency | list[Currency]) -> bool:
        if isinstance(data, list):
            self.db.extend(data)
        else:
            self.db.append(data)

        return True

