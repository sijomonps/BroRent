from typing import Dict


def unread_notifications_count(request) -> Dict[str, int]:
    """Provide unread notifications count globally in templates.

    Returns 0 for anonymous users.
    """
    user = getattr(request, 'user', None)
    if not user or not user.is_authenticated or not user.pk:
        return {"unread_notifications_count": 0}

    # Lazy import to avoid circulars during app loading
    from .models import Notification

    count = Notification.objects.filter(user=user, read=False).count()
    return {"unread_notifications_count": count}


