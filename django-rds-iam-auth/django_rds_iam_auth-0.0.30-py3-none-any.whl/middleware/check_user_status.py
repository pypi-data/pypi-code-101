from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework.response import Response


class CheckUserStatusMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if isinstance(request.user, AnonymousUser) or request.user.is_active:
            response = self.get_response(request)
        else:
            response = Response(status=status.HTTP_403_FORBIDDEN, data={
                'message': 'Current user is not active'
            })

        return response
