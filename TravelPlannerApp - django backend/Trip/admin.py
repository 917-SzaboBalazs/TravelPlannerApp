from django.contrib import admin

from Trip.models import Trip, AccommodationType, Accommodation, Activity, TransportationType, Transportation

# Register your models here.

admin.site.register(Trip)
admin.site.register(AccommodationType)
admin.site.register(Accommodation)
admin.site.register(Activity)
admin.site.register(TransportationType)
admin.site.register(Transportation)
