from django.urls import path

from Trip.views import ListCreateTripView, RetrieveUpdateDestroyTripView, ListCreateAccommodationView, \
    RetrieveUpdateDestroyAccommodationView, ListCreateActivityView, RetrieveUpdateDestroyActivityView

urlpatterns = [
    path('trips/', ListCreateTripView.as_view(), name="all_trips"),
    path('trips/<int:pk>', RetrieveUpdateDestroyTripView.as_view(), name="trip_details"),
    path('accommodations/', ListCreateAccommodationView.as_view(), name="all_accommodations"),
    path('accommodations/<int:pk>', RetrieveUpdateDestroyAccommodationView.as_view(), name="accommodation_details"),
    path('activities/', ListCreateActivityView.as_view(), name="all_activities"),
    path('activities/<int:pk>', RetrieveUpdateDestroyActivityView.as_view(), name="activity_details"),
]
