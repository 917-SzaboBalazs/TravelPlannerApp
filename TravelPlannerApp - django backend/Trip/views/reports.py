from django.db import models
from django.db.models import Avg, F, Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Trip.models.trips import Trip
from Trip.serializers import AverageDurationOfTripsInDaysSerializer, TripsTotalPriceOfActivitiesSerializer, \
    TripsBasedOnAverageComfortOfTransportationsSerializer


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
