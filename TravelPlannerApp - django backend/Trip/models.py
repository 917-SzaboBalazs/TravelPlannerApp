from django.db import models

# Create your models here.


class AccommodationType(models.Model):

    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Accommodation(models.Model):

    type = models.ForeignKey(to=AccommodationType, on_delete=models.PROTECT, related_name="accom_ids")
    name = models.CharField(max_length=60)
    no_stars = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    price_per_night = models.FloatField(null=True, blank=True)
    check_in_time = models.TimeField(default="14:00:00", null=True, blank=True)
    check_out_time = models.TimeField(default="10:00:00", null=True, blank=True)

    def __str__(self):
        return self.name + " (" + str(self.type) + ")"


class Activity(models.Model):

    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    no_persons = models.IntegerField(null=True, blank=True)
    has_instructor = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class TransportationType(models.Model):

    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Transportation(models.Model):

    SPEED_CHOICES = (
        ("SLOW", "SLOW"),
        ("MEDIUM", "MEDIUM"),
        ("FAST", "FAST"),
    )

    name = models.CharField(max_length=60)
    type = models.ForeignKey(to=TransportationType, on_delete=models.PROTECT, related_name="transport_ids")
    price = models.FloatField(null=True, blank=True)
    speed = models.CharField(max_length=10, choices=SPEED_CHOICES, null=True, blank=True)
    comfort_level = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name + " (" + str(self.type) + ")"


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
    accommodations = models.ManyToManyField(to=Accommodation, blank=True, related_name="accommodations")
    budget = models.FloatField(null=True, blank=True)
    activities = models.ManyToManyField(to=Activity, blank=True, related_name="activities")
    transportations = models.ManyToManyField(to=Transportation, blank=True, related_name="transportations")
    notes = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name + " (" + self.destination + " | " + str(self.start_date) + " - " + str(self.end_date) + ")"
