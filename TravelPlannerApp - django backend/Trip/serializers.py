from rest_framework import serializers
from rest_framework_dataclasses.serializers import DataclassSerializer

from Trip.models import Trip, Accommodation, Activity, AccommodationType, Transportation, TransportationType
from Trip.reports import AverageDurationOfTripsInDays, TripsTotalPriceOfActivities, \
    TripsBasedOnAverageComfortOfTransportations


# ================== Model serializers ===========================


class TripListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ["id", "name", "destination", "start_date", "end_date", "budget", "notes", ]

    def validate(self, data):

        if data["start_date"] is not None and data["end_date"] is not None and data["start_date"] > data["end_date"]:
            raise serializers.ValidationError("finish must occur after start")

        if data["budget"] is not None and data["budget"] < 0.:
            raise serializers.ValidationError("budget must be a non-negative float number")

        return data


class TripDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = "__all__"
        depth = 2

    def validate(self, data):

        if data["start_date"] is not None and data["end_date"] is not None and data["start_date"] > data["end_date"]:
            raise serializers.ValidationError("finish must occur after start")

        if data["budget"] is not None and data["budget"] < 0.:
            raise serializers.ValidationError("budget must be a non-negative float number")

        return data


class AccommodationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationType
        fields = "__all__"


class TransportationTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransportationType
        fields = "__all__"


class AccommodationSerializer(serializers.ModelSerializer):
    type_id = serializers.PrimaryKeyRelatedField(queryset=AccommodationType.objects.all(), write_only=True)

    class Meta:
        model = Accommodation
        fields = "__all__"
        depth = 1

    def validate(self, data):
        if data["no_stars"] is not None and (data["no_stars"] < 1 or data["no_stars"] > 5):
            raise serializers.ValidationError("number of stars must be between 1 and 5")

        if data["price_per_night"] is not None and data["price_per_night"] < 0.:
            raise serializers.ValidationError("price/night must be a non-negative float number")

        return data

    def create(self, validated_data):
        validated_data['type_id'] = validated_data['type_id'].id

        accommodation = Accommodation.objects.create(**validated_data)
        accommodation.save()

        return accommodation

    def update(self, instance, validated_data):
        validated_data['type_id'] = validated_data['type_id'].id
        [setattr(instance, k, v) for k, v in validated_data.items()]
        instance.save()

        return instance


class TransportationSerializer(serializers.ModelSerializer):
    type_id = serializers.PrimaryKeyRelatedField(queryset=TransportationType.objects.all(), write_only=True)

    class Meta:
        model = Transportation
        fields = "__all__"
        depth = 1

    def validate(self, data):

        if data["price"] is not None and data["price"] < 0.:
            raise serializers.ValidationError("price must be a non-negative float number")

        if data["comfort_level"] is not None and (data["comfort_level"] < 1 or data["comfort_level"] > 5):
            raise serializers.ValidationError("comfort level must be between 1 and 5")

        return data

    def create(self, validated_data):
        validated_data['type_id'] = validated_data['type_id'].id

        transportation = Transportation.objects.create(**validated_data)
        transportation.save()

        return transportation

    def update(self, instance, validated_data):
        validated_data['type_id'] = validated_data['type_id'].id
        [setattr(instance, k, v) for k, v in validated_data.items()]
        instance.save()

        return instance


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
