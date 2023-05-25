from django.urls import path

from Trip.views.report_views import AverageDurationOfTripsInDaysView, TripsTotalPriceOfActivitiesView, \
    SortTripsBasedOnAverageComfortOfTransportations
from Trip.views.activity_views import ListCreateActivityView, RetrieveUpdateDestroyActivityView
from Trip.views.transportation_views import ListCreateTransportationView, RetrieveUpdateDestroyTransportationView
from Trip.views.accommodation_views import ListCreateAccommodationView, RetrieveUpdateDestroyAccommodationView
from Trip.views.trip_views import ListCreateTripView, RetrieveUpdateDestroyTripView, BulkDeleteTripsByIDsView, \
    BudgetPredictionView
from Trip.views.profile_views import UserProfileView
from Trip.views.user_views import ListUsersView, UpdateUserView

urlpatterns = [
    path('trips/', ListCreateTripView.as_view(), name="trip_list"),
    path('trips/<int:pk>/', RetrieveUpdateDestroyTripView.as_view(), name="trip_details"),
    path('trips/bulk_delete/', BulkDeleteTripsByIDsView.as_view(), name="bulk_delete_trips"),

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

    path('users/<int:pk>/profile/', UserProfileView.as_view(), name="user_profile_view"),

    path('users/', ListUsersView.as_view(), name="list_users_view"),
    path('users/<int:pk>/', UpdateUserView.as_view(), name="update_user_view"),

    path('predict-budget/', BudgetPredictionView.as_view(), name='budget-prediction'),
]

