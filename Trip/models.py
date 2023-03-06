from django.db import models

"""
Entity: Trip

Attributes:

Trip ID (unique identifier for each trip)
Destination (the location the user is traveling to)
Start Date (the date the user plans to begin the trip)
End Date (the date the user plans to end the trip)
Accommodation (the type of accommodation the user wants to stay in, such as hotel, hostel, or vacation rental)
Budget (the maximum amount the user is willing to spend on the trip)
Activities (a list of activities the user is interested in doing while on the trip)
Transportation (the mode of transportation the user plans to use to get to and around the destination)
Notes (additional notes or comments the user wants to make about the trip)
"""

# Create your models here.


class Trip(models.Model):

    destination = models.CharField(max_length=60)
    start_date = models.DateField()
    end_date = models.DateField()
    accommodation = models.CharField(max_length=60)
    budget = models.FloatField()
    activities = models.CharField(max_length=120)
    transportation = models.CharField(max_length=120)
    notes = models.CharField(max_length=500)


class AccommodationType(models.Model):
    name = models.CharField(max_length=60)


class Accommodation(models.Model):

    type = models.OneToOneField(to=AccommodationType, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    no_stars = models.IntegerField()
    location = models.CharField(max_length=150)
    price_per_night = models.FloatField()
    room_number = models.IntegerField()


class Activity(models.Model):

    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    no_persons = models.IntegerField()
    has_instructor = models.BooleanField(default=False)
