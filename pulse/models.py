from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        USER = "user", "User"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class PriceAlert(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        TRIGGERED = "triggered", "Triggered"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="alerts",
    )

    origin = models.CharField(max_length=10)

    destination = models.CharField(max_length=10)

    threshold_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.origin}-{self.destination}"
            f" @ ₹{self.threshold_price}"
        )


class NotificationLog(models.Model):

    alert = models.ForeignKey(
        PriceAlert,
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    triggered_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    message = models.TextField()

    notified_at = models.DateTimeField(
        auto_now_add=True,
    )
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message