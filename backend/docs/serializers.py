from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Document

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined",
        )


class DocumentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Document
        fields = (
            "id",
            "text",
            "user",
            "date_created",
        )
