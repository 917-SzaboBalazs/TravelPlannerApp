from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from Trip.models.trips import Trip
from Trip.serializers import TripListSerializer, TripDetailSerializer


class ListCreateTripView(ListCreateAPIView):

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

    def get_serializer_class(self):
        return TripListSerializer


class RetrieveUpdateDestroyTripView(RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripDetailSerializer

    def get_serializer_context(self):
        return {
            'method': self.request.method
        }
