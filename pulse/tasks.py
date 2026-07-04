from celery import shared_task

from .models import PriceAlert, NotificationLog
from .services import MockFlightService


@shared_task
def check_price_alerts():

    alerts = PriceAlert.objects.filter(
        status=PriceAlert.Status.ACTIVE
    )

    checked = 0
    notifications = 0

    for alert in alerts:

        result = MockFlightService.search_flights(
            origin=alert.origin,
            destination=alert.destination,
        )

        checked += 1

        current_price = result["price"]

        if current_price <= alert.threshold_price:

            NotificationLog.objects.create(
                 alert=alert,
                 triggered_price=current_price,
                 message=(
                    f"Price dropped to ₹{current_price} "
                    f"for {alert.origin} → {alert.destination}"
    ),
)

            notifications += 1

    return {
        "checked": checked,
        "notifications": notifications,
    }