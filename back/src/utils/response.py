from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
from django.http import HttpResponseForbidden


def build_bad_request_response(msg: str) -> Response:
    return Response(msg, status=status.HTTP_401_UNAUTHORIZED)


def build_forbidden_response(msg: str) -> Response:
    return HttpResponseForbidden(msg)


class JsonResponseOk(JsonResponse):
    """
    Extending from JsonResponse class.
    Returns status code 200.
    """

    def __init__(self, data=None) -> None:
        super().__init__(data, status=status.HTTP_200_OK, safe=False)


class JsonResponseCreated(JsonResponse):
    """
    Extending from JsonResponse class.
    Returns status code 201.
    """

    def __init__(self, data=None) -> None:
        super().__init__(data, status=status.HTTP_201_CREATED, safe=False)


class JsonResponseBadRequest(JsonResponse):
    """
    Extending from JsonResponse class.
    Returns status code 400.
    """

    def __init__(self, data=None) -> None:
        super().__init__(data, status=status.HTTP_400_BAD_REQUEST, safe=False)
