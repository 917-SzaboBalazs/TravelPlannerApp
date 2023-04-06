from rest_framework import serializers

from Trip.models.accommodation import Accommodation, AccommodationType
from Trip.serializers.custom_model_serializers import CustomModelSerializer


class AccommodationSerializer(CustomModelSerializer):

    class Meta:
        model = Accommodation
        fields = "__all__"

    def validate(self, data):
        if data["no_stars"] is not None and (data["no_stars"] < 1 or data["no_stars"] > 5):
            raise serializers.ValidationError("number of stars must be between 1 and 5")

        if data["price_per_night"] is not None and data["price_per_night"] < 0.:
            raise serializers.ValidationError("price/night must be a non-negative float number")

        return data


class AccommodationTypeSerializer(CustomModelSerializer):
    class Meta:
        model = AccommodationType
        fields = "__all__"
