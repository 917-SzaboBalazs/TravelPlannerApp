from django.contrib import admin

from Trip.models.trip import Trip
from Trip.models.accommodation import AccommodationType, Accommodation
from Trip.models.transportation import TransportationType, Transportation
from Trip.models.activity import Activity

# Register your models here.

admin.site.register(Trip)
admin.site.register(AccommodationType)
admin.site.register(Accommodation)
admin.site.register(Activity)
admin.site.register(TransportationType)
admin.site.register(Transportation)
