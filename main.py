import asyncio
from concurrent import futures

import grpc
from grpc import aio

from config import RPC_PORT
from src.database import get_async_session
from pkg.grpc.src.currency import model_pb2_grpc
from src.currency.grpc import CurrencyServices
from pkg.logger.iLogger import ILogger
from pkg.logger.logger import Logger

logger: ILogger = Logger()


async def serve():
    server = aio.server(futures.ThreadPoolExecutor(max_workers=10))
    # server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    currency_service: CurrencyServices = CurrencyServices(logger, await get_async_session())
    model_pb2_grpc.add_CurrencyServicesServicer_to_server(currency_service, server)
    server.add_insecure_port(f'[::]:{RPC_PORT}')
    logger.info('start server')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(serve())
