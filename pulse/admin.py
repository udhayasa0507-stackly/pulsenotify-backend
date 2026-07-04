from django.contrib import admin

from .models import (
    UserProfile,
    PriceAlert,
    NotificationLog,
)

admin.site.register(UserProfile)
admin.site.register(PriceAlert)
admin.site.register(NotificationLog)