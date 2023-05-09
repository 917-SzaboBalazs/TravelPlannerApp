from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ("M", "M"),
        ("F", "F"),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    activation_code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return "Profile of " + str(self.user)
