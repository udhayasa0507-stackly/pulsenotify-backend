from django.urls import path

from .views import (
    RegisterAPIView,
    LoginAPIView,
    PriceAlertListCreateAPIView,
    PriceAlertDeleteAPIView,
    FlightSearchAPIView,
    AdminSummaryAPIView,
    NotificationListAPIView,
    NotificationDeleteAPIView,
)

urlpatterns = [
    path("auth/register/", RegisterAPIView.as_view(), name="register"),
    path("auth/login/", LoginAPIView.as_view(), name="login"),

    path(
        "alerts/",
        PriceAlertListCreateAPIView.as_view(),
        name="alerts",
    ),

    path(
        "alerts/<int:pk>/",
        PriceAlertDeleteAPIView.as_view(),
        name="delete-alert",
    ),

    path(
    "flights/search/",
    FlightSearchAPIView.as_view(),
    name="flight-search",
),

    path(
    "admin/summary/",
    AdminSummaryAPIView.as_view(),
    name="admin-summary",
),

    path(
    "notifications/",
    NotificationListAPIView.as_view(),
    name="notifications",
),

    path(
    "notifications/<int:pk>/",
    NotificationDeleteAPIView.as_view(),
    name="notification-delete",
),
]