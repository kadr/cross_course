import abc

from services.currecy.const import Currency as CurrencyType


class IRepository(abc.ABC):
    @abc.abstractmethod
    def get_all(self, sort: str = 'ASC') -> list[CurrencyType]: ...


class Currency:
    repository: IRepository

    def __init__(self, repository: IRepository):
        self.repository = repository

    def get_last_currency(self) -> CurrencyType:
        result: list[CurrencyType] = self.repository.get_all("DESC")
        if not result:
            return []
        return result[-1]
