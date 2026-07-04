from django.contrib.auth.models import User
from rest_framework import serializers

from .models import PriceAlert,NotificationLog


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )


class PriceAlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = PriceAlert
        fields = [
            "id",
            "origin",
            "destination",
            "threshold_price",
            "status",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "status",
            "created_at",
        ]

class FlightSearchSerializer(serializers.Serializer):

    origin = serializers.CharField(max_length=10)
    destination = serializers.CharField(max_length=10)


class AdminSummarySerializer(serializers.Serializer):

    total_users = serializers.IntegerField()
    total_alerts = serializers.IntegerField()
    active_alerts = serializers.IntegerField()
    inactive_alerts = serializers.IntegerField()
    total_notifications = serializers.IntegerField()

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationLog
        fields = [
            "id",
            "message",
            "created_at",
        ]