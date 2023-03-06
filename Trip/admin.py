from django.contrib import admin

from Trip.models import Trip, AccommodationType, Accommodation, Activity

# Register your models here.

admin.site.register(Trip)
admin.site.register(AccommodationType)
admin.site.register(Accommodation)
admin.site.register(Activity)
