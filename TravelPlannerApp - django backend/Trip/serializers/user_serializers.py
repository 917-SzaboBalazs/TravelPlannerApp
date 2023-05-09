from datetime import datetime

from rest_framework import serializers
from django.contrib.auth import get_user_model
import random
import string


import re
from Trip.models.users import UserProfile
from Trip.serializers.custom_model_serializers import CustomModelSerializer


class UserProfileSerializer(CustomModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

    def validate(self, data):
        phone_number_pattern = re.compile("^[0-9]*$")

        if "phone_number" in data and data["phone_number"] is not None and \
                phone_number_pattern.match(data["phone_number"]):
            raise serializers.ValidationError("Phone number can only contain letters.")

        if "birthday" in data and data["birthday"] is not None and \
                data["birthday"] < datetime(1900, 1, 1):
            raise serializers.ValidationError("Birthday date must be greater than 1st Jan 1900")

        return True


class UserSerializer(CustomModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "password", "is_superuser", "is_staff", "is_active", ]

    def create(self, validated_data):
        validated_data["is_active"] = False
        password = validated_data.pop("password")
        new_user = get_user_model().objects.create(**validated_data)
        new_user.set_password(password)
        new_user.save()

        new_user_profile = UserProfile.objects.create(user_id=new_user.id,
                                                      activation_code=self.generate_activation_code())
        new_user_profile.save()

        return new_user

    def generate_activation_code(self):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for i in range(10))

        return random_string
