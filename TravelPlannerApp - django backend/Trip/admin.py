from django.contrib import admin

from Trip.models.trips import Trip
from Trip.models.accommodations import AccommodationType, Accommodation
from Trip.models.transportations import TransportationType, Transportation
from Trip.models.activities import Activity

# Register your models here.

admin.site.register(Trip)
admin.site.register(AccommodationType)
admin.site.register(Accommodation)
admin.site.register(Activity)
admin.site.register(TransportationType)
admin.site.register(Transportation)
