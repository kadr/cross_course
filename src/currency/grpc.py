from google.protobuf.json_format import MessageToDict
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from pkg.grpc.src.currency.model_pb2 import GetCurrencyRequest, GetCurrencyResponse, Currency as CurrencyPB, \
    AddCurrencyRequest, GetCurrenciesResponse
from pkg.grpc.src.currency.model_pb2_grpc import CurrencyServicesServicer
from pkg.logger.iLogger import ILogger
from src.currency.models import Currency


class CurrencyServices(CurrencyServicesServicer):
    session: AsyncSession
    logger: ILogger

    def __init__(self, logger: ILogger, session: AsyncSession):
        self.session = session
        self.logger = logger

    async def GetCurrency(self, request: GetCurrencyRequest, context) -> GetCurrencyResponse:
        self.logger.info('GetCurrency')
        query = select(Currency).filter(Currency.id == request.id)
        res = (await self.session.execute(query)).first()
        if not res:
            context.set_code(2)
            context.set_details('Записи не найдены')
            return GetCurrencyResponse()
        currency = res[0]

        return GetCurrencyResponse(currency=CurrencyServices.get_currency_response(currency))

    async def GetCurrencies(self, request, context) -> GetCurrenciesResponse:
        self.logger.info('GetCurrencies')
        query = select(Currency).order_by(desc(Currency.create_at))
        res = (await self.session.execute(query)).all()
        if not res:
            context.set_code(2)
            context.set_details('Записи не найдены')
            return GetCurrenciesResponse()
        currency_response: list[CurrencyPB] = []
        for currency in res:
            currency: Currency = currency[0]
            currency_response.append(CurrencyServices.get_currency_response(currency))
        return GetCurrenciesResponse(currency=currency_response)

    async def AddCurrency(self, request: AddCurrencyRequest, context):
        self.logger.info('AddCurrency')
        currency = Currency(**MessageToDict(request, preserving_proto_field_name=True))
        self.session.add(currency)
        await self.session.commit()
        await self.session.refresh(currency)

        return GetCurrencyResponse(currency=CurrencyServices.get_currency_response(currency))

    @staticmethod
    def get_currency_response(currency) -> CurrencyPB:
        return CurrencyPB(id=currency.id, iso=currency.iso, currency_name=currency.currency_name,
                          is_obsolete=currency.is_obsolete, superseded_by=currency.superseded_by,
                          currency_symbol=currency.currency_symbol,
                          currency_symbol_on_right=currency.currency_symbol_on_right,
                          create_at=currency.create_at)
