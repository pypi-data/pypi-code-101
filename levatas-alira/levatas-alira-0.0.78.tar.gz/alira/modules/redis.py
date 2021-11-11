import os
import redis

from rq import Queue

from alira.modules import module


class RedisModule(module.Module):
    def __init__(
        self,
        module_id,
        model_identifier,
        configuration_directory,
        redis_server: str,
    ):
        super().__init__(module_id)

        self.model_identifier = model_identifier
        self.configuration_directory = configuration_directory
        self.redis_server = redis_server
        self.queue_name = model_identifier

    def get_redis_queue(self):
        if self.redis_server:
            redis_connection = redis.from_url(self.redis_server)
            return Queue(self.queue_name, connection=redis_connection, is_async=True)

        return None


class ServiceException(Exception):
    """
    We raise this exception when we can't connect to a third-party, online service.
    We expect this to happen whenever there's no internet connection.

    This exception is useful to reattempt operations when they are being processed
    by the Redis queue.
    """
    pass