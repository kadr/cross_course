from __future__ import annotations

import logging

import psycopg2

from services.currecy.currency import IRepository, Currency


class RepositoryPgSql(IRepository):
    connection: psycopg2.connection

    def __init__(self, connection: psycopg2.connection):
        self.connection = connection

    def get_all(self, sort: str = 'ASC') -> list[Currency]:
        cursor: psycopg2.cursor = self.connection.cursor()
        select_sql: str = f'SELECT * FROM currency ORDER BY id {sort}'
        cursor.execute(select_sql)
        return cursor.fetchmany()
