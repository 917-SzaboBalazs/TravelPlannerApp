from rest_framework import serializers

from Trip.models import Trip, Accommodation, Activity


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = "__all__"


class AccommodationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accommodation
        fields = "__all__"


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = "__all__"
