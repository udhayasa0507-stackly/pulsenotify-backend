from rest_framework.permissions import BasePermission


class IsAdminUserProfile(BasePermission):
    """
    Allow only users whose profile role is ADMIN.
    """

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        return (
            hasattr(request.user, "profile")
            and request.user.profile.role == "ADMIN"
        )