from .models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["avatar"]
