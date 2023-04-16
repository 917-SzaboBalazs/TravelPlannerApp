from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomPagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        return Response(data=data, status=status.HTTP_200_OK)

    def get_count(self, queryset):
        return 99999999
