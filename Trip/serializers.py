from rest_framework import serializers

from Trip.models import Trip


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ['id', 'destination', 'start_date', 'end_date', 'accommodation', 'budget', 'transportation', 'notes', ]
