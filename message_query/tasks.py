from __future__ import annotations

import asyncio

from celery import Celery
from message_query import celery_settings
from celery.schedules import crontab

from pkg.logger.iLogger import ILogger
from pkg.logger.logger import Logger
from services.xe_currency.start import start

logger: ILogger = Logger()

app = Celery('tasks')
app.config_from_object(celery_settings, namespace='CELERY')
app.conf.beat_schedule = {
    'xe-request-every-minute': {
        'task': 'message_query.tasks.xe_request',
        'schedule': crontab(minute='*/60', day_of_week='mon-fri')
    }
}


@app.task
def xe_request() -> None:
    asyncio.run(start(logger))
