from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, UpdateAPIView

from TravelPlannerApp.permissions import IsAdminUser
from Trip.serializers.user_serializers import UserSerializer


class ListUsersView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by("-id")


class UpdateUserView(UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()
