import unittest

from async_jaeger import ConstSampler, Tracer
from async_jaeger.reporter import NullReporter
from opentracing.harness.api_check import APICompatibilityCheckMixin


class APITest(unittest.TestCase, APICompatibilityCheckMixin):

    reporter = NullReporter()
    sampler = ConstSampler(True)
    _tracer = Tracer(
        service_name='test_service_1', reporter=reporter, sampler=sampler)

    def tracer(self):
        return APITest._tracer

    def test_binary_propagation(self):
        # TODO binary codecs are not implemented at the moment
        pass

    def is_parent(self, parent, span):
        return span.parent_id == getattr(parent, 'span_id', None)
