from rest_framework import serializers

from Trip.models.trip import Trip
from Trip.serializers.custom_model_serializers import CustomModelSerializer


class TripSerializer(CustomModelSerializer):

    class Meta:
        model = Trip

    def validate(self, data):

        if "start_date" in data and "end_date" in data and data["start_date"] is not None and data["end_date"] \
                is not None and data["start_date"] > data["end_date"]:
            raise serializers.ValidationError("finish must occur after start")

        if "budget" in data and data["budget"] is not None and data["budget"] < 0.:
            raise serializers.ValidationError("budget must be a non-negative float number")

        return data
