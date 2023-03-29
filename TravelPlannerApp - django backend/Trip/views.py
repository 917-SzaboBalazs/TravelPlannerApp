from datetime import datetime, timedelta

from django.db import models
from django.db.models import Avg, F, Count
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Trip.models import Trip, Accommodation, Activity, AccommodationType, TransportationType, Transportation
from Trip.serializers import TripListSerializer, ActivitySerializer, \
    AccommodationTypeSerializer, \
    TransportationTypeSerializer, TransportationSerializer, AverageDurationOfTripsInDaysSerializer, \
    TripsTotalPriceOfActivitiesSerializer, TripsBasedOnAverageComfortOfTransportationsSerializer, TripDetailSerializer, \
    AccommodationSerializer


# Create your views here.

# ================= Trip =====================


class ListCreateTripView(ListCreateAPIView):
    serializer_class = TripListSerializer

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
    serializer_class = TripDetailSerializer


# ============================================


# ============== Accommodation =================


class ListCreateAccommodationView(ListCreateAPIView):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer


class RetrieveUpdateDestroyAccommodationView(RetrieveUpdateDestroyAPIView):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer


class ListAddAccommodationView(APIView):

    def get(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')

        try:
            queryset = Trip.objects.get(id=trip_id).accommodations.values()

            for query in queryset:
                query['type'] = AccommodationType.objects.get(id=query['type_id'])
                del query['type_id']

            serializer = AccommodationSerializer(queryset, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Trip.DoesNotExist as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')

        try:
            accommodation = Accommodation.objects.get(id=request.data['accommodation_id'])

            Trip.objects.get(id=trip_id).accommodations.add(accommodation.id)
            serializer = AccommodationSerializer(accommodation)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except (Trip.DoesNotExist, Accommodation.DoesNotExist) as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)


class RemoveAccommodationFromTripView(APIView):

    def delete(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')
        accommodation_id = self.kwargs.get('acc_id')

        try:
            Trip.objects.get(id=trip_id).accommodations.remove(Accommodation.objects.get(id=accommodation_id))

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Trip.DoesNotExist as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *arg, **kwargs):
        trip_id = self.kwargs.get('pk')
        accommodation_id = self.kwargs.get('acc_id')

        try:
            instance = Trip.objects.get(id=trip_id).accommodations.get(id=accommodation_id)
            serializer = AccommodationSerializer(instance=instance)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except (Trip.DoesNotExist, Accommodation.DoesNotExist) as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)

# ======================================


# ============== Transportation views =================


class ListCreateTransportationView(ListCreateAPIView):
    queryset = Transportation.objects.all()
    serializer_class = TransportationSerializer


class RetrieveUpdateDestroyTransportationView(RetrieveUpdateDestroyAPIView):
    queryset = Transportation.objects.all()
    serializer_class = TransportationSerializer


class ListAddTransportationView(APIView):

    def get(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')

        try:
            queryset = Trip.objects.get(id=trip_id).transportations.values()

            for query in queryset:
                query['type'] = TransportationType.objects.get(id=query['type_id'])
                del query['type_id']

            serializer = TransportationSerializer(queryset, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Trip.DoesNotExist as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')

        try:
            transportation = Transportation.objects.get(id=request.data['transportation_id'])

            Trip.objects.get(id=trip_id).transportations.add(transportation.id)
            serializer = TransportationSerializer(transportation)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except (Trip.DoesNotExist, Transportation.DoesNotExist) as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)


class RemoveTransportationFromTripView(APIView):

    def delete(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')
        transportation_id = self.kwargs.get('transport_id')

        try:
            Trip.objects.get(id=trip_id).transportations.remove(Transportation.objects.get(id=transportation_id))

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Trip.DoesNotExist as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')
        transportation_id = self.kwargs.get('transport_id')

        try:
            instance = Trip.objects.get(id=trip_id).transportations.get(id=transportation_id)
            serializer = TransportationSerializer(instance=instance)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except (Trip.DoesNotExist, Transportation.DoesNotExist) as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)

# ======================================


# ====================== Activity views ================


class ListCreateActivityView(ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class RetrieveUpdateDestroyActivityView(RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ListAddActivityView(APIView):

    def get(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')

        try:
            queryset = Trip.objects.get(id=trip_id).activities.values()
            serializer = ActivitySerializer(queryset, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Trip.DoesNotExist as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')

        try:
            activity = Activity.objects.get(id=request.data['activity_id'])

            Trip.objects.get(id=trip_id).activities.add(activity.id)
            serializer = ActivitySerializer(activity)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except (Trip.DoesNotExist, Activity.DoesNotExist) as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)


class RemoveActivityFromTripView(APIView):

    def delete(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')
        activity_id = self.kwargs.get('act_id')

        try:
            Trip.objects.get(id=trip_id).activities.remove(Activity.objects.get(id=activity_id))

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Trip.DoesNotExist as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')
        activity_id = self.kwargs.get('act_id')

        try:
            instance = Trip.objects.get(id=trip_id).activities.get(id=activity_id)
            serializer = ActivitySerializer(instance=instance)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except (Trip.DoesNotExist, Activity.DoesNotExist) as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)


# =====================================


# ==================== Report views =========================

class AverageDurationOfTripsInDaysView(APIView):

    def get(self, request):
        """
        This view is used to get the average duration of all trips in days,
        as well as the total number of trips, by calculating the difference
        between the start date and end date of each trip.
        """

        data = Trip.objects.all().filter(start_date__isnull=False, end_date__isnull=False)\
            .aggregate(
            average_duration=Avg(
                F('end_date') - F('start_date'),
                output_field=models.FloatField()
            ) / 1000 / 1000 / 60 / 60 / 24,
            number_of_trips=Count('id')
        )

        if data["number_of_trips"] == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Number of trips with start_data and "
                                                                                 "end_data specified must be greater "
                                                                                 "than 0"})

        serializer = AverageDurationOfTripsInDaysSerializer(data=data)

        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class TripsTotalPriceOfActivitiesView(APIView):
    def get(self, request):
        """
        This view will return a list of trips, sorted by the
        total price of activities associated with each trip.
        """
        trip_queryset = Trip.objects.all()
        data = list()

        for trip in trip_queryset:
            total_price = 0.0

            for activity in trip.activities.all().values():
                if activity['price'] is not None:
                    total_price += activity['price']

            data.append({
                "name": trip.name,
                "total_price": total_price
            })

        data.sort(key=lambda x: -x.get('total_price'))

        serializer = TripsTotalPriceOfActivitiesSerializer(data=data, many=True)

        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class SortTripsBasedOnAverageComfortOfTransportations(APIView):
    def get(self, request):
        trip_queryset = Trip.objects.all()
        data = list()

        for trip in trip_queryset:
            total_comfort = 0

            for transportation in trip.transportations.all().values():
                if transportation['comfort_level'] is not None:
                    total_comfort += transportation['comfort_level']

            no_trips = trip_queryset.count()
            if no_trips == 0:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={
                    "message": "No trips to show"
                })

            average_comfort = total_comfort / no_trips

            data.append({
                "name": trip.name,
                "average_comfort": average_comfort
            })

        data.sort(key=lambda x: -x.get('average_comfort'))

        serializer = TripsBasedOnAverageComfortOfTransportationsSerializer(data=data, many=True)

        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


# =========================================
