from concurrent import futures

import grpc

from currency.grpc import CurrencyServices
from ..pkg.grpc.src.currency import model_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    model_pb2_grpc.add_CurrencyServicesServicer_to_server(CurrencyServices(), server)
    server.add_insecure_port('[::]:5000')
    server.start()
    server.wait_for_termination()


if __name__ == '__mane__':
    serve()