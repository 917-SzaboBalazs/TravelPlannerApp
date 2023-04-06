from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from Trip.models.trip import Trip
from Trip.serializers.trip_serializers import TripSerializer


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

    def get_serializer_context(self):
        if self.request.method == "GET":
            return {
                "depth": 0,
                "exclude": ("accommodations", "transportations", "activities", ),
            }

        return {
            "exclude": (),
            "depth": 0,
        }


class RetrieveUpdateDestroyTripView(RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get_serializer_context(self):
        return {
            "depth": 2 if self.request.method == "GET" else 0,
            "exclude": (),
        }
