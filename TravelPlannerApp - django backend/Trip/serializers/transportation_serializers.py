from rest_framework import serializers

from Trip.models.transportation import Transportation, TransportationType
from Trip.serializers.custom_model_serializers import CustomModelSerializer


class TransportationSerializer(CustomModelSerializer):

    class Meta:
        model = Transportation
        fields = "__all__"

    def validate(self, data):

        if data["price"] is not None and data["price"] < 0.:
            raise serializers.ValidationError("price must be a non-negative float number")

        if data["comfort_level"] is not None and (data["comfort_level"] < 1 or data["comfort_level"] > 5):
            raise serializers.ValidationError("comfort level must be between 1 and 5")

        return data


class TransportationTypeSerializer(CustomModelSerializer):
    class Meta:
        model = TransportationType
        fields = "__all__"
