from django.db import models


class AccommodationType(models.Model):

    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Accommodation(models.Model):

    type = models.ForeignKey(to=AccommodationType, on_delete=models.PROTECT)
    name = models.CharField(max_length=60)
    no_stars = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    price_per_night = models.FloatField(null=True, blank=True)
    check_in_time = models.TimeField(default="14:00:00", null=True, blank=True)
    check_out_time = models.TimeField(default="10:00:00", null=True, blank=True)

    def __str__(self):
        return self.name + " (" + str(self.type) + ")"
