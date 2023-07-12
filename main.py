import os

from fastapi import FastAPI
from dotenv import load_dotenv

app = FastAPI()
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


"""
1. Пишем тест для сервиса получения данных из внешнего api  XE  
2. Описываем модель данных валют для сохранения ее в базу.
3. Реализую метод получения данных из api.
4. Реализую метод записи данный из api в базу.
5. 

  
Необходимо разработать микросервис на fastapi, который периодически опрашивает api XE.com и сохраняет данные в таблицу 
по валюте (для теста достаточно 10 любых валют) и сохраняет в БД кросс курс каждой валютной пары каждый час.
Для доступа к данным необходимо подготовить ендпоинт отображаюий последний кросс-курс переданной пары 
(имя в url, а не query)
Предусмотреть повтор сбора при ошибке доступа к XE через 3 минуты.
"""
