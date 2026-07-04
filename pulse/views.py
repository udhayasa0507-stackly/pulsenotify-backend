from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import generics
from .models import PriceAlert,NotificationLog
from django.shortcuts import get_object_or_404

from .services import MockFlightService
from .serializers import FlightSearchSerializer,AdminSummarySerializer,PriceAlertSerializer, RegisterSerializer
from .permissions import IsAdminUserProfile
from .models import NotificationLog
from .serializers import NotificationSerializer


class RegisterAPIView(APIView):

    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "username": user.username,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "role": user.profile.role,
            },
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(APIView):

    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):

        username = request.data.get("username")

        password = request.data.get("password")

        user = authenticate(
            username=username,
            password=password,
        )

        if not user:
            return Response(
                {
                    "message": "Invalid credentials."
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "username": user.username,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "role": user.profile.role,
            }
        )
    
class PriceAlertCreateAPIView(generics.CreateAPIView):

    serializer_class = PriceAlertSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PriceAlertListAPIView(generics.ListAPIView):

    serializer_class = PriceAlertSerializer

    def get_queryset(self):
        return PriceAlert.objects.filter(
            user=self.request.user
        ).order_by("-created_at")
    
class PriceAlertDeleteAPIView(APIView):

    def delete(self, request, pk):

        alert = get_object_or_404(
            PriceAlert,
            id=pk,
            user=request.user,
        )

        alert.status = PriceAlert.Status.INACTIVE

        alert.save()

        return Response(
            {
                "status": "inactive"
            },
            status=status.HTTP_200_OK,
        )
    
class PriceAlertListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = PriceAlertSerializer

    def get_queryset(self):
        return PriceAlert.objects.filter(
            user=self.request.user
        ).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FlightSearchAPIView(APIView):

    def post(self, request):

        serializer = FlightSearchSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        result = MockFlightService.search_flights(
            origin=data["origin"],
            destination=data["destination"],
        )

        return Response(result)
    
class AdminSummaryAPIView(APIView):

    permission_classes = [IsAdminUserProfile]

    def get(self, request):

        data = {
            "total_users": User.objects.count(),
            "total_alerts": PriceAlert.objects.count(),
            "active_alerts": PriceAlert.objects.filter(
                status=PriceAlert.Status.ACTIVE
            ).count(),
            "inactive_alerts": PriceAlert.objects.filter(
                status=PriceAlert.Status.INACTIVE
            ).count(),
            "total_notifications": NotificationLog.objects.count(),
        }

        serializer = AdminSummarySerializer(data)

        return Response(serializer.data)
    
class NotificationListAPIView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return NotificationLog.objects.filter(
            alert__user=self.request.user
        ).order_by("-notified_at")
    
class NotificationDeleteAPIView(APIView):

    def delete(self, request, pk):
        notification = get_object_or_404(
            NotificationLog,
            id=pk,
            user=request.user,
        )
        notification.delete()
        return Response(
            {
                "message": "Deleted"
            },
            status=status.HTTP_200_OK,
        )