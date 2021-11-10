import time

import pytest
from opentracing import Tracer as NoopTracer
from async_jaeger.tracer import Tracer
from async_jaeger.reporter import NullReporter
from async_jaeger.sampler import ConstSampler


def _generate_spans(tracer, iterations=1000, sleep=None):
    for i in range(0, iterations):
        span = tracer.start_trace(operation_name='root-span')
        span.finish()
        if sleep is not None:
            t = time.time() + sleep
            while time.time() < t:
                pass


@pytest.mark.skip()
def test_noop_tracer(benchmark):
    tracer = NoopTracer()
    benchmark(_generate_spans, tracer)


@pytest.mark.skip()
def test_no_sampling(benchmark):
    tracer = Tracer.default_tracer(
        channel=None, service_name='benchmark',
        reporter=NullReporter(), sampler=ConstSampler(False))
    benchmark(_generate_spans, tracer)


@pytest.mark.skip()
def test_100pct_sampling(benchmark):
    tracer = Tracer.default_tracer(
        channel=None, service_name='benchmark',
        reporter=NullReporter(), sampler=ConstSampler(True))
    benchmark(_generate_spans, tracer)


@pytest.mark.skip()
def test_100pct_sampling_250mcs(benchmark):
    tracer = Tracer.default_tracer(
        channel=None, service_name='benchmark',
        reporter=NullReporter(), sampler=ConstSampler(True))
    # 250 micros for request execution
    benchmark(_generate_spans, tracer, sleep=0.00025)


@pytest.mark.skip()
def test_all_batched_size10(benchmark):
    from tchannel.sync import TChannel
    ch = TChannel(name='foo')
    f = ch.advertise(routers=['127.0.0.1:21300', '127.0.0.1:21301'])
    f.result()
    tracer = Tracer.default_tracer(ch, service_name='benchmark',
                                   sampler=ConstSampler(True))
    tracer.reporter.batch_size = 10
    # 250 micros for request execution
    benchmark(_generate_spans, tracer, sleep=0.00025)


@pytest.mark.skip()
def test_all_batched_size5(benchmark):
    from tchannel.sync import TChannel
    ch = TChannel(name='foo')
    f = ch.advertise(routers=['127.0.0.1:21300', '127.0.0.1:21301'])
    f.result()
    tracer = Tracer.default_tracer(ch, service_name='benchmark',
                                   sampler=ConstSampler(True))
    tracer.reporter.batch_size = 5
    # 250 micros for request execution
    benchmark(_generate_spans, tracer, sleep=0.00025)


@pytest.mark.skip()
def test_all_not_batched(benchmark):
    from tchannel.sync import TChannel
    ch = TChannel(name='foo')
    f = ch.advertise(routers=['127.0.0.1:21300', '127.0.0.1:21301'])
    f.result()
    tracer = Tracer.default_tracer(ch, service_name='benchmark', sampler=ConstSampler(True))
    tracer.reporter.batch_size = 1
    # 250 micros for request execution
    benchmark(_generate_spans, tracer, sleep=0.00025)
