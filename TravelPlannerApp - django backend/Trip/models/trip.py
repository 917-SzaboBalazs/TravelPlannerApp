from django.db import models

from Trip.models.accommodation import Accommodation
from Trip.models.activity import Activity
from Trip.models.transportation import Transportation


class Trip(models.Model):
    """
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

    name = models.CharField(max_length=60)
    destination = models.CharField(max_length=60, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    budget = models.FloatField(null=True, blank=True)
    accommodations = models.ManyToManyField(to=Accommodation, blank=True)
    activities = models.ManyToManyField(to=Activity, blank=True)
    transportations = models.ManyToManyField(to=Transportation, blank=True)
    notes = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name + " (" + self.destination + " | " + str(self.start_date) + " - " + str(self.end_date) + ")"
