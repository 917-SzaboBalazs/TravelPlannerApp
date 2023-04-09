from rest_framework_dataclasses.serializers import DataclassSerializer

from Trip.models.reports import AverageDurationOfTripsInDays, TripsTotalPriceOfActivities, \
    TripsBasedOnAverageComfortOfTransportations


class AverageDurationOfTripsInDaysSerializer(DataclassSerializer):
    class Meta:
        dataclass = AverageDurationOfTripsInDays


class TripsTotalPriceOfActivitiesSerializer(DataclassSerializer):
    class Meta:
        dataclass = TripsTotalPriceOfActivities


class TripsBasedOnAverageComfortOfTransportationsSerializer(DataclassSerializer):
    class Meta:
        dataclass = TripsBasedOnAverageComfortOfTransportations
