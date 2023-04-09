from django.urls import path

from Trip.views.report_views import AverageDurationOfTripsInDaysView, TripsTotalPriceOfActivitiesView, \
    SortTripsBasedOnAverageComfortOfTransportations
from Trip.views.activity_views import ListCreateActivityView, RetrieveUpdateDestroyActivityView, ListAddActivityView, \
    RemoveActivityFromTripView
from Trip.views.transportation_views import ListCreateTransportationView, RetrieveUpdateDestroyTransportationView, \
    ListAddTransportationView, RemoveTransportationFromTripView
from Trip.views.accommodation_views import ListCreateAccommodationView, RetrieveUpdateDestroyAccommodationView, \
    ListAddAccommodationView, RemoveAccommodationFromTripView
from Trip.views.trip_views import ListCreateTripView, RetrieveUpdateDestroyTripView

urlpatterns = [
    path('trips/', ListCreateTripView.as_view(), name="trip_list"),
    path('trips/<int:pk>/', RetrieveUpdateDestroyTripView.as_view(), name="trip_details"),
    path('trips/<int:pk>/accommodations/', ListAddAccommodationView.as_view(), name="trip_accommodation_list"),
    path('trips/<int:pk>/accommodations/<int:acc_id>/', RemoveAccommodationFromTripView.as_view(),
         name="trip_remove_accommodation_from_list"),
    path('trips/<int:pk>/transportations/', ListAddTransportationView.as_view(), name="trip_transportation_list"),
    path('trips/<int:pk>/transportations/<int:transport_id>/', RemoveTransportationFromTripView.as_view(),
         name="trip_remove_activity_from_list"),
    path('trips/<int:pk>/activities/', ListAddActivityView.as_view(), name="trip_activity_list"),
    path('trips/<int:pk>/activities/<int:act_id>/', RemoveActivityFromTripView.as_view(),
         name="trip_remove_activity_from_list"),

    path('accommodations/', ListCreateAccommodationView.as_view(), name="accommodation_list"),
    path('accommodations/<int:pk>/', RetrieveUpdateDestroyAccommodationView.as_view(), name="accommodation_details"),

    path('transportations/', ListCreateTransportationView.as_view(), name="transportation_list"),
    path('transportations/<int:pk>/', RetrieveUpdateDestroyTransportationView.as_view(), name="transportation_details"),

    path('activities/', ListCreateActivityView.as_view(), name="activity_list"),
    path('activities/<int:pk>/', RetrieveUpdateDestroyActivityView.as_view(), name="activity_details"),

    path('reports/avg_duration_of_trips_in_days/', AverageDurationOfTripsInDaysView.as_view(),
         name="avg_duration_of_trips_in_days"),
    path('reports/trips_total_price_of_activities/', TripsTotalPriceOfActivitiesView.as_view(),
         name="trips_total_price_of_activities"),
    path('reports/trips_based_on_average_comfort_of_transportations/',
         SortTripsBasedOnAverageComfortOfTransportations.as_view(),
         name="trips_based_on_average_comfort_of_transportations"),
]

