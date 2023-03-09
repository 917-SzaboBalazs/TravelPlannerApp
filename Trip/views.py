from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from Trip.models import Trip, Accommodation, Activity
from Trip.serializers import TripSerializer, AccommodationSerializer, ActivitySerializer


# Create your views here.


class ListCreateTripView(ListCreateAPIView):

    serializer_class = TripSerializer

    def get_queryset(self):
        """
        The function "get_queryset" returns a filtered queryset of Trip objects based on the provided max_budget
        parameter in the request query parameters. It filters the queryset to include only Trip objects whose
        budget field is less than or equal to the provided max_budget value.
        """
        queryset = Trip.objects.all()
        max_budget = self.request.query_params.get('max_budget')

        if max_budget is not None:
            queryset = queryset.filter(budget__lte=max_budget)

        return queryset


class RetrieveUpdateDestroyTripView(RetrieveUpdateDestroyAPIView):

    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class ListCreateAccommodationView(ListCreateAPIView):

    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer


class RetrieveUpdateDestroyAccommodationView(RetrieveUpdateDestroyAPIView):

    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer


class ListCreateActivityView(ListCreateAPIView):

    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class RetrieveUpdateDestroyActivityView(RetrieveUpdateDestroyAPIView):

    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
