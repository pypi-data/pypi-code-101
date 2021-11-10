import logging
from .metrics import MetricsFactory


MINIMUM_CREDITS = 1.0
default_logger = logging.getLogger(__name__)


class Throttler(object):
    def set_client_id(self, client_id: int) -> None:
        """
        Called by tracer to set client ID of throttler.
        """
        pass

    def is_allowed(self, operation: str) -> bool:
        raise NotImplementedError()

    def close(self) -> None:
        pass


class ThrottlerMetrics(object):
    """
    Metrics specific to throttler.
    """

    def __init__(self, metrics_factory: MetricsFactory) -> None:
        self.throttled_debug_spans = \
            metrics_factory.create_counter(name='jaeger:throttled_debug_spans')
        self.throttler_update_success = \
            metrics_factory.create_counter(name='jaeger:throttler_update',
                                           tags={'result': 'ok'})
        self.throttler_update_failure = \
            metrics_factory.create_counter(name='jaeger:throttler_update',
                                           tags={'result': 'err'})
