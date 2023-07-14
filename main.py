from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from pkg.logger.iLogger import ILogger
from pkg.logger.logger import Logger
from src.currency.router import router as router_currency, RecordNotFoundError, router_cross_course

logger: ILogger = Logger()
app = FastAPI()


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    message = f"Что то пошло не так. {exc}"
    status = 500
    if isinstance(exc, RecordNotFoundError):
        status = 404
        message = str(exc)
    return JSONResponse(status_code=status, content={"message": message})


app.include_router(router_currency)
app.include_router(router_cross_course)

"""
1. Пишем тест для сервиса получения данных из внешнего api XE  
1. Пишем тест для метода сохранения данный в базу, даем ему фейковую базу.  
2. Описываем модель данных валют для сохранения ее в базу.
3. Реализую метод получения данных из api.
4. Реализую метод записи данный из api в базу.
5. Тест для метода получения последнего кросс-курса переданной пары
6. Сам метод получения последнего кросс-курса переданной пары

  
Необходимо разработать микросервис на fastapi, который периодически опрашивает api XE.com и сохраняет данные в таблицу 
по валюте (для теста достаточно 10 любых валют) и сохраняет в БД кросс курс каждой валютной пары каждый час.
Для доступа к данным необходимо подготовить ендпоинт отображаюий последний кросс-курс переданной пары 
(имя в url, а не query)
Предусмотреть повтор сбора при ошибке доступа к XE через 3 минуты.
"""
