from django.db.models import Count
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from Trip.models.trip import Trip
from Trip.serializers.trip_serializers import TripSerializer, ListTripSerializer


class ListCreateTripView(ListCreateAPIView):
    serializer_class = ListTripSerializer

    def get_queryset(self):
        queryset = Trip.objects.annotate(
            number_of_accommodations=Count('accommodations', distinct=True),
            number_of_transportations=Count('transportations', distinct=True),
            number_of_activities=Count('activities', distinct=True)
        ).values(
            'id', 'name', 'destination', 'start_date', 'end_date', 'budget', 'notes',
            'number_of_accommodations', 'number_of_transportations', 'number_of_activities'
        ).order_by('-id')

        return queryset

    def get_serializer_context(self):
        if self.request.method == "GET":
            return {
                "depth": 0,
                "fields": ("id", "name", "destination", "start_date", "end_date", "budget", "notes",
                           "number_of_accommodations", "number_of_transportations", "number_of_activities",)
            }

        return {
            "fields": ("id", "name", "destination", "start_date", "end_date", "budget", "notes", "accommodations",
                       "transportations", "activities", "number_of_accommodations", "number_of_transportations",
                       "number_of_activities"),
            "depth": 0,
        }


class RetrieveUpdateDestroyTripView(RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.prefetch_related("accommodations", "transportations", "activities",
                                             "accommodations__type", "transportations__type")
    serializer_class = TripSerializer

    def get_serializer_context(self):
        return {
            "depth": 2 if self.request.method == "GET" else 0,
            "fields": ("id", "name", "destination", "start_date", "end_date", "budget", "notes", "accommodations",
                       "transportations", "activities",)
        }
