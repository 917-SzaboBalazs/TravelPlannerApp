from django.db import models


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
    type = models.ForeignKey(to=TransportationType, on_delete=models.PROTECT)
    price = models.FloatField(null=True, blank=True)
    speed = models.CharField(max_length=10, choices=SPEED_CHOICES, null=True, blank=True)
    comfort_level = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name + " (" + str(self.type) + ")"
