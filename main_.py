# from fastapi import FastAPI, Request
# from starlette.responses import JSONResponse

from pkg.logger.iLogger import ILogger
from pkg.logger.logger import Logger
# from src.currency.router import router as router_currency, RecordNotFoundError, router_cross_course

logger: ILogger = Logger()


# app = FastAPI()


# @app.exception_handler(Exception)
# async def exception_handler(request: Request, exc: Exception):
#     message = f"Что то пошло не так. {exc}"
#     status = 500
#     if isinstance(exc, RecordNotFoundError):
#         status = 404
#         message = str(exc)
#     return JSONResponse(status_code=status, content={"message": message})


# app.include_router(router_currency)
# app.include_router(router_cross_course)
