import asyncpg
from asyncpg import Connection


class Pgsql:
    _connection: None
    db: str
    user: str
    password: str
    host: str

    def __init__(self, db: str, user: str, password: str, host: str):
        self.db, self.user, self.password, self.host = db, user, password, host

    @property
    async def connection(self) -> Connection:
        self._connection: Connection = await asyncpg.connect(database=self.db, user=self.user, password=self.password,
                                                             host=self.host)
        try:
            await self._connection.execute('SELECT 1')
        except asyncpg.InterfaceError as err:
            raise PgSqlConnectionError('Не удалось подключиться к базе данный.')

        return self._connection


class PgSqlConnectionError(Exception): ...
