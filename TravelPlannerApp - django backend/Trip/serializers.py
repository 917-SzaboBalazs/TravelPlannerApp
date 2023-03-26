from rest_framework import serializers
from rest_framework_dataclasses.serializers import DataclassSerializer

from Trip.models import Trip, Accommodation, Activity, AccommodationType, Transportation, TransportationType
from Trip.reports import AverageDurationOfTripsInDays, TripsTotalPriceOfActivities, \
    TripsBasedOnAverageComfortOfTransportations


# ================== Model serializers ===========================

class AccommodationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accommodation
        fields = "__all__"

    def validate(self, data):
        if data["no_stars"] is not None and (data["no_stars"] < 1 or data["no_stars"] > 5):
            raise serializers.ValidationError("number of stars must be between 1 and 5")

        if data["price_per_night"] is not None and data["price_per_night"] < 0.:
            raise serializers.ValidationError("price/night must be a non-negative float number")

        return data


class AccommodationTypeSerializer(serializers.ModelSerializer):
    accom_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = AccommodationType
        fields = "__all__"


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = "__all__"

    def validate(self, data):
        if data["price"] is not None and data["price"] < 0.:
            raise serializers.ValidationError("price must be a non-negative float number")

        if data["no_persons"] is not None and data["no_persons"] <= 0:
            raise serializers.ValidationError("number of persons must be greater than 0")

        return data


class TransportationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transportation
        fields = "__all__"

    def validate(self, data):

        if data["price"] is not None and data["price"] < 0.:
            raise serializers.ValidationError("price must be a non-negative float number")

        if data["comfort_level"] is not None and (data["comfort_level"] < 1 or data["comfort_level"] > 5):
            raise serializers.ValidationError("comfort level must be between 1 and 5")

        return data


class TransportationTypeSerializer(serializers.ModelSerializer):
    transport_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = TransportationType
        fields = "__all__"


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = "__all__"

    def validate(self, data):

        if data["start_date"] is not None and data["end_date"] is not None and data["start_date"] > data["end_date"]:
            raise serializers.ValidationError("finish must occur after start")

        if data["budget"] is not None and data["budget"] < 0.:
            raise serializers.ValidationError("budget must be a non-negative float number")

        return data

# ==============================================================

# ================== DTO serializers ===========================


class AverageDurationOfTripsInDaysSerializer(DataclassSerializer):

    class Meta:
        dataclass = AverageDurationOfTripsInDays


class TripsTotalPriceOfActivitiesSerializer(DataclassSerializer):

    class Meta:
        dataclass = TripsTotalPriceOfActivities


class TripsBasedOnAverageComfortOfTransportationsSerializer(DataclassSerializer):

    class Meta:
        dataclass = TripsBasedOnAverageComfortOfTransportations

# ===============================================
