from async_jaeger import SpanContext


def test_parent_id_to_none():
    ctx1 = SpanContext(trace_id=1, span_id=2, parent_id=0, flags=1)
    assert ctx1.parent_id is None


def test_with_baggage_items():
    baggage1 = {'x': 'y'}
    ctx1 = SpanContext(trace_id=1, span_id=2, parent_id=3, flags=1,
                       baggage=baggage1)
    ctx2 = ctx1.with_baggage_item('a', 'b')
    assert ctx1.trace_id == ctx2.trace_id
    assert ctx1.span_id == ctx2.span_id
    assert ctx1.parent_id == ctx2.parent_id
    assert ctx1.flags == ctx2.flags
    assert ctx1.baggage != ctx2.baggage
    baggage1['a'] = 'b'
    assert ctx1.baggage == ctx2.baggage

    ctx3 = ctx2.with_baggage_item('a', None)
    assert ctx2.baggage != ctx3.baggage
    baggage1.pop('a')
    assert ctx3.baggage == baggage1
