import asyncio
import os

from pkg.repository.pgsql import Pgsql
from services.xe_currency.api import XECurrency
from services.xe_currency.repository_pgsql import RepositoryPgSql

RECONNECT_TIMEOUT_SEC: int = 3*60
PARSE_TIMEOUT_SEC: int = 60*60

db, user, password, host = os.getenv("PGSQL_DB"),os.getenv("PGSQL_USER"),os.getenv("PGSQL_PASSWORD"),\
                           os.getenv("PGSQL_HOST")
api_id, api_key = os.getenv('XE_API_ID'), os.getenv('XE_API_KEY')
pgsql: Pgsql = Pgsql(db, user, password, host)
repository: RepositoryPgSql = RepositoryPgSql(pgsql.connection)
xe_currency_api: XECurrency = XECurrency(repository, api_id, api_key)



if __name__ == '__main__':
    asyncio.run(xe_currency_api.get_currencies())
