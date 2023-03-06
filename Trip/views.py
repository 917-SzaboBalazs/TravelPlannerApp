from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from Trip.models import Trip
from Trip.serializers import TripSerializer

# Create your views here.


class ListCreateTripView(ListCreateAPIView):

    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class RetrieveUpdateDestroyTripView(RetrieveUpdateDestroyAPIView):

    queryset = Trip.objects.all()
    serializer_class = TripSerializer
