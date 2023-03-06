from django.urls import path

from Trip.views import ListCreateTripView, RetrieveUpdateDestroyTripView

urlpatterns = [
    path('', ListCreateTripView.as_view(), name="all_trips"),
    path('<int:pk>', RetrieveUpdateDestroyTripView.as_view(), name="trip_details"),
]
