import psycopg2


class Pgsql:
    _connection: None

    def __init__(self, db: str, user: str, password: str, host: str):
        self._connection = psycopg2.connect(dbname=db, user=user, password=password, host=host)
        try:
            cur = self._connection.cursor()
            cur.execute('SELECT 1')
        except (psycopg2.OperationalError, psycopg2.InterfaceError) as err:
            raise PgSqlConnectionError('Не удалось подключиться к базе данный.')

    @property
    def connection(self):
        return self._connection


class PgSqlConnectionError(Exception): ...
