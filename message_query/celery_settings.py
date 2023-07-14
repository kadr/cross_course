import os

redis_password = os.getenv('REDIS_PASSWORD')
redis_host = os.getenv('REDIS_HOST')

if not redis_password or not redis_host:
    raise Exception('both REDIS_HOST and REDIS_PASSWORD should be provided your env')

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_HOST', f'redis://:{redis_password}@{redis_host}/0')
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = os.getenv('CURRENT_TIMEZONE')
CELERY_ENABLE_UTC = False
