from rest_framework.generics import RetrieveAPIView, CreateAPIView
from Trip.serializers.user_serializers import UserProfileSerializer, UserSerializer
from Trip.models.users import UserProfile

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model


class UserProfileView(RetrieveAPIView):

    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.all()


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()


class ActivateAccountView(APIView):

    def get(self, request, confirmation_code):
        try:
            user_profile = UserProfile.objects.get(activation_code=confirmation_code)
        except UserProfile.DoesNotExist:
            return Response(data={"message": "Invalid code"}, status=status.HTTP_400_BAD_REQUEST)

        user = get_user_model().objects.get(id=user_profile.user_id)

        user.is_active = True
        user_profile.activation_code = ""

        user.save()
        user_profile.save()

        return Response(data={"message": "Account activated"}, status=status.HTTP_200_OK)

