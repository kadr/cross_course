FROM python:3.10

RUN mkdir /app
WORKDIR /app

COPY ./requirements ./requirements

RUN python -m pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --no-cache-dir -r ./requirements/base.txt

COPY . .


ENV PYTHONPATH "/app:/app/lib:/app/tests"


EXPOSE 8000

CMD /usr/bin/python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
