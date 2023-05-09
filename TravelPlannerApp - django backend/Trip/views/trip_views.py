from django.db.models import Count, F
from rest_framework import status, serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.response import Response

from Trip.models.trip import Trip
from Trip.serializers.trip_serializers import TripSerializer, ListTripSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from TravelPlannerApp.permissions import IsOwnerOrReadOnly, IsModeratorUser, IsAdminUser


class ListCreateTripView(ListCreateAPIView):
    serializer_class = ListTripSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        print(request.data)

        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Trip.objects.annotate(
            number_of_accommodations=Count('accommodations', distinct=True),
            number_of_transportations=Count('transportations', distinct=True),
            number_of_activities=Count('activities', distinct=True),
            username=F('user__username')
        ).select_related('user').order_by('-id')

        return queryset

    def get_serializer_context(self):
        if self.request.method == "GET":
            return {
                "depth": 0,
                "fields": ("id", "name", "destination", "start_date", "end_date", "budget", "notes",
                           "number_of_accommodations", "number_of_transportations", "number_of_activities", "user_id", "username")
            }

        return {
            "fields": ("id", "name", "destination", "start_date", "end_date", "budget", "notes", "accommodations",
                       "transportations", "activities", "number_of_accommodations", "number_of_transportations",
                       "number_of_activities", "user", "username"),
            "depth": 0,
        }


class RetrieveUpdateDestroyTripView(RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.prefetch_related("accommodations", "transportations", "activities",
                                             "accommodations__type", "transportations__type")
    serializer_class = TripSerializer
    permission_classes = [IsModeratorUser | IsOwnerOrReadOnly]

    def get_serializer_context(self):
        return {
            "depth": 2 if self.request.method == "GET" else 0,
            "fields": ("id", "name", "destination", "start_date", "end_date", "budget", "notes", "accommodations",
                       "transportations", "activities", "user", )
        }


class BulkDeleteTripsByIDsView(DestroyAPIView):
    queryset = Trip.objects.all()
    lookup_url_kwarg = 'ids'
    lookup_field = 'id__in'
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(serializer.validated_data['ids'])
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, ids):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(id__in=ids)
        queryset.delete()

    def get_serializer(self, *args, **kwargs):
        return self.get_serializer_class()(*args, **kwargs)

    def get_serializer_class(self):
        class SerializerClass(serializers.Serializer):
            ids = serializers.ListField(child=serializers.IntegerField())

            def create(self, validated_data):
                pass

            def update(self, instance, validated_data):
                pass

        return SerializerClass
