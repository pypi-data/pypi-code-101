import opentracing
from opentracing import Tracer, Format


def test_new_trace():
    tracer = Tracer()

    span = tracer.start_span(operation_name='test')
    span.set_baggage_item('Fry', 'Leela')
    span.set_tag('x', 'y')
    span.log_event('z')

    child = tracer.start_span(operation_name='child',
                              references=opentracing.child_of(span.context))
    child.log_event('w')
    assert child.get_baggage_item('Fry') is None
    carrier = {}
    tracer.inject(
        span_context=child.context,
        format=Format.TEXT_MAP,
        carrier=carrier)
    assert carrier == dict()
    child.finish()

    span.finish()


def test_join_trace():
    tracer = Tracer()

    span_ctx = tracer.extract(format=Format.TEXT_MAP, carrier={})
    span = tracer.start_span(operation_name='test',
                             references=opentracing.child_of(span_ctx))
    span.set_tag('x', 'y')
    span.set_baggage_item('a', 'b')
    span.log_event('z')

    child = tracer.start_span(operation_name='child',
                              references=opentracing.child_of(span.context))
    child.log_event('w')
    child.finish()

    span.finish()
