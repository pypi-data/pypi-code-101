from celery import Celery as AsyncTask


def get_async_task(app_name: str, broker: str = None, backend: str = None) -> AsyncTask:
    return AsyncTask(app_name, broker=broker, backend=backend)
