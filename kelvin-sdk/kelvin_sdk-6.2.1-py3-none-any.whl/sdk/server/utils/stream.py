from typing import Any, Callable

from starlette.responses import StreamingResponse


def build_stream_response(call: Callable, **kwargs: Any) -> StreamingResponse:
    """
    Yields a stream response by building a generator with a callable that returns an OperationResponse with a stream
    attribute.

    Parameters
    ----------
    call : Callable
        Function that returns an OperationResponse with a stream
    kwargs : Any
        Keyword arguments for the callable

    Returns
    -------
    StreamingResponse
        a StreamingResponse object

    """

    def stream_generator() -> Any:
        response = call(**kwargs)
        log_stream = response.stream
        if log_stream:
            for item in log_stream:
                yield item

    return StreamingResponse(stream_generator(), media_type="text/event-stream")
