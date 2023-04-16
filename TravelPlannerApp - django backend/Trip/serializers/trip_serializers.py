from rest_framework import serializers

from Trip.models.trip import Trip
from Trip.serializers.custom_model_serializers import CustomModelSerializer


class ListTripSerializer(CustomModelSerializer):

    number_of_accommodations = serializers.SerializerMethodField()
    number_of_transportations = serializers.SerializerMethodField()
    number_of_activities = serializers.SerializerMethodField()

    class Meta:
        model = Trip

    def get_number_of_accommodations(self, obj):
        return obj.accommodations.count()

    def get_number_of_transportations(self, obj):
        return obj.transportations.count()

    def get_number_of_activities(self, obj):
        return obj.activities.count()

    def validate(self, data):

        if "start_date" in data and "end_date" in data and data["start_date"] is not None and data["end_date"] \
                is not None and data["start_date"] > data["end_date"]:
            raise serializers.ValidationError("finish must occur after start")

        if "budget" in data and data["budget"] is not None and data["budget"] < 0.:
            raise serializers.ValidationError("budget must be a non-negative float number")

        if len(data["accommodations"]) > 10:
            raise serializers.ValidationError("maximum number of accommodations is 10")

        if len(data["transportations"]) > 10:
            raise serializers.ValidationError("maximum number of transportations is 10")

        if len(data["activities"]) > 10:
            raise serializers.ValidationError("maximum number of activities is 10")

        return data


class TripSerializer(CustomModelSerializer):

    class Meta:
        model = Trip

    def validate(self, data):

        if "start_date" in data and "end_date" in data and data["start_date"] is not None and data["end_date"] \
                is not None and data["start_date"] > data["end_date"]:
            raise serializers.ValidationError("finish must occur after start")

        if "budget" in data and data["budget"] is not None and data["budget"] < 0.:
            raise serializers.ValidationError("budget must be a non-negative float number")

        if len(data["accommodations"]) > 10:
            raise serializers.ValidationError("maximum number of accommodations is 10")

        if len(data["transportations"]) > 10:
            raise serializers.ValidationError("maximum number of transportations is 10")

        if len(data["activities"]) > 10:
            raise serializers.ValidationError("maximum number of activities is 10")

        return data
