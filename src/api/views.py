from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class APIHealthView(APIView):
    """View to test if API is online."""

    @extend_schema(
        responses={
            status.HTTP_200_OK: "",
        },
    )
    def get(self, request: Request):
        """Point to test if API is online."""
        return Response(status=status.HTTP_200_OK)
