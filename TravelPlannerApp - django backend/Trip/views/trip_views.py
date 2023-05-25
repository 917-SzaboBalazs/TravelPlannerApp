import os

import torch
import pandas as pd
from django.db.models import Count, F
from rest_framework import status, serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from sklearn.preprocessing import StandardScaler
from torch import nn
import pickle

from Trip.models.trip import Trip
from Trip.serializers.trip_serializers import TripSerializer, ListTripSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from TravelPlannerApp.permissions import IsOwnerOrReadOnly, IsModeratorUser, IsAdminUser


class ListCreateTripView(ListCreateAPIView):
    serializer_class = ListTripSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        print(request.data)

        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Trip.objects.annotate(
            number_of_accommodations=Count('accommodations', distinct=True),
            number_of_transportations=Count('transportations', distinct=True),
            number_of_activities=Count('activities', distinct=True),
            username=F('user__username')
        ).select_related('user').order_by('-id')

        return queryset

    def get_serializer_context(self):
        if self.request.method == "GET":
            return {
                "depth": 0,
                "fields": ("id", "name", "destination", "start_date", "end_date", "budget", "notes",
                           "number_of_accommodations", "number_of_transportations", "number_of_activities", "user_id", "username")
            }

        return {
            "fields": ("id", "name", "destination", "start_date", "end_date", "budget", "notes", "accommodations",
                       "transportations", "activities", "number_of_accommodations", "number_of_transportations",
                       "number_of_activities", "user", "username"),
            "depth": 0,
        }


class RetrieveUpdateDestroyTripView(RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.prefetch_related("accommodations", "transportations", "activities",
                                             "accommodations__type", "transportations__type")
    serializer_class = TripSerializer
    permission_classes = [IsModeratorUser | IsOwnerOrReadOnly]

    def get_serializer_context(self):
        return {
            "depth": 2 if self.request.method == "GET" else 0,
            "fields": ("id", "name", "destination", "start_date", "end_date", "budget", "notes", "accommodations",
                       "transportations", "activities", "user", )
        }


class BulkDeleteTripsByIDsView(DestroyAPIView):
    queryset = Trip.objects.all()
    lookup_url_kwarg = 'ids'
    lookup_field = 'id__in'
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(serializer.validated_data['ids'])
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, ids):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(id__in=ids)
        queryset.delete()

    def get_serializer(self, *args, **kwargs):
        return self.get_serializer_class()(*args, **kwargs)

    def get_serializer_class(self):
        class SerializerClass(serializers.Serializer):
            ids = serializers.ListField(child=serializers.IntegerField())

            def create(self, validated_data):
                pass

            def update(self, instance, validated_data):
                pass

        return SerializerClass


# Get the directory path of the current view file
current_directory = os.path.dirname(os.path.abspath(__file__))


# Define the deep learning model
class BudgetPredictor(nn.Module):
    def __init__(self):
        super(BudgetPredictor, self).__init__()
        self.fc1 = nn.Linear(2, 16)
        self.fc2 = nn.Linear(16, 8)
        self.fc3 = nn.Linear(8, 1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x


# Create a new class-based view that inherits from `APIView`
class BudgetPredictionView(APIView):
    def get(self, request):
        # Load the saved model
        model_path = os.path.join(current_directory, 'budget_predictor_model.pth')
        state_dict = torch.load(model_path)

        # Recreate the model instance
        model = BudgetPredictor()
        model.load_state_dict(state_dict)
        model.eval()

        # Retrieve the input parameters from the request query parameters
        destination = request.GET.get('destination')
        start_date = pd.to_datetime(request.GET.get('start_date'))
        end_date = pd.to_datetime(request.GET.get('end_date'))

        # Preprocess the input data
        # Convert start_date and end_date to numerical values (days since the earliest date)
        earliest_date = pd.to_datetime('01/01/1970')  # Replace with the earliest date used during training
        start_date = (start_date - earliest_date).days
        end_date = (end_date - earliest_date).days

        # Create the input tensor
        input_tensor = torch.tensor([[start_date, end_date]], dtype=torch.float32)

        # Perform inference
        with torch.no_grad():
            predicted_budget = model(input_tensor)

        # Load the scaling parameters
        scaler_path = os.path.join(current_directory, 'scaler_params.pkl')

        with open(scaler_path, 'rb') as f:
            scaler_mean, scaler_std = pickle.load(f)

        # Create a new StandardScaler object and set the saved scaling parameters
        scaler = StandardScaler()
        scaler.mean_ = scaler_mean
        scaler.scale_ = scaler_std

        # Cast the predicted budget to an integer
        predicted_budget = scaler.inverse_transform(predicted_budget.numpy())
        predicted_budget = int(predicted_budget.item())

        # Return the predicted budget as an integer in the API response
        return Response({'predicted_budget': predicted_budget})
