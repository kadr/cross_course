from __future__ import annotations

import psycopg2

from services.xe_currency.api import IRepository
from services.xe_currency.const import Currency


class RepositoryPgSql(IRepository):
    connection: psycopg2.connection

    def __init__(self, connection: psycopg2.connection):
        self.connection = connection

    def create(self, data: Currency | list[Currency]) -> bool:
        cursor: psycopg2.cursor = self.connection.cursor()
        insert_sql: str = 'INSERT INTO currency (iso, currency_name, is_obsolete, ' \
                          'superseded_by,currency_symbol, currency_symbol_on_right) ' \
                          'VALUES (%s,%s,%b,%s,%s,%b)'
        values: list[tuple[str, str, bool, str, str, bool]] = []
        if isinstance(data, list):
            for value in data:
                values.append(((value.get('iso'), value.get('currency_name'), value.get('is_obsolete'),
                                value.get('superseded_by'), value.get('currency_symbol'),
                                value.get('currency_symbol_on_right'))))
        else:
            values.append((data.get('iso'), data.get('currency_name'), data.get('is_obsolete'),
                           data.get('superseded_by'), data.get('currency_symbol'),
                           data.get('currency_symbol_on_right')))

        cursor.executemany(insert_sql, values)
        self.connection.commit()
        if cursor.rowcount:
            return True

        return False
