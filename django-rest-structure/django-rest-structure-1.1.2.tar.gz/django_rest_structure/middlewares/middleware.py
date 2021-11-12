import uuid
from django.utils import timezone
from ..logs.console import emmit


class RequestHandlerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.request_uid = uuid.uuid4()
        request_time = timezone.now()

        response = self.get_response(request)
        emmit(request, response, response.err if hasattr(response, 'err') else None, request_time, timezone.now())
        return response
