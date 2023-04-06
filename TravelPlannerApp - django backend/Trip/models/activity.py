from django.db import models


class Activity(models.Model):

    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    no_persons = models.IntegerField(null=True, blank=True)
    has_instructor = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
