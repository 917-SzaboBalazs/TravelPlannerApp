from rest_framework import serializers

from Trip.models.activity import Activity
from Trip.serializers.custom_model_serializers import CustomModelSerializer


class ActivitySerializer(CustomModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"

    def validate(self, data):
        if data["price"] is not None and data["price"] < 0.:
            raise serializers.ValidationError("price must be a non-negative float number")

        if data["no_persons"] is not None and data["no_persons"] <= 0:
            raise serializers.ValidationError("number of persons must be greater than 0")

        return data
