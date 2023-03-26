from django.urls import path

from Trip.views import ListCreateTripView, RetrieveUpdateDestroyTripView, ListCreateAccommodationView, \
    RetrieveUpdateDestroyAccommodationView, ListCreateActivityView, RetrieveUpdateDestroyActivityView, \
    ListCreateAccommodationTypeView, RetrieveUpdateDestroyAccommodationTypeView, ListCreateTransportationTypeView, \
    RetrieveUpdateDestroyTransportationTypeView, ListCreateTransportationView, RetrieveUpdateDestroyTransportationView, \
    AverageDurationOfTripsInDaysView, TripsTotalPriceOfActivitiesView, SortTripsBasedOnAverageComfortOfTransportations

urlpatterns = [
    path('trips/', ListCreateTripView.as_view(), name="all_trips"),
    path('trips/<int:pk>/', RetrieveUpdateDestroyTripView.as_view(), name="trip_details"),

    path('accommodation_types/', ListCreateAccommodationTypeView.as_view(), name="all_accommodation_types"),
    path('accommodation_types/<int:pk>/', RetrieveUpdateDestroyAccommodationTypeView.as_view(),
         name="accommodation_type_details"),

    path('accommodations/', ListCreateAccommodationView.as_view(), name="all_accommodations"),
    path('accommodations/<int:pk>/', RetrieveUpdateDestroyAccommodationView.as_view(), name="accommodation_details"),

    path('activities/', ListCreateActivityView.as_view(), name="all_activities"),
    path('activities/<int:pk>/', RetrieveUpdateDestroyActivityView.as_view(), name="activity_details"),

    path('transportation_types/', ListCreateTransportationTypeView.as_view(), name="all_transportation_types"),
    path('transportation_types/<int:pk>/', RetrieveUpdateDestroyTransportationTypeView.as_view(),
         name="transportation_type_details"),

    path('transportations/', ListCreateTransportationView.as_view(), name="all_transportations"),
    path('transportations/<int:pk>/', RetrieveUpdateDestroyTransportationView.as_view(), name="transportation_details"),

    path('reports/avg_duration_of_trips_in_days/', AverageDurationOfTripsInDaysView.as_view(),
         name="avg_duration_of_trips_in_days"),
    path('reports/trips_total_price_of_activities/', TripsTotalPriceOfActivitiesView.as_view(),
         name="trips_total_price_of_activities"),
    path('reports/trips_based_on_average_comfort_of_transportations/',
         SortTripsBasedOnAverageComfortOfTransportations.as_view(),
         name="trips_based_on_average_comfort_of_transportations"),
]

