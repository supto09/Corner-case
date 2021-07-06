from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrAuthenticatedReadOnly(BasePermission):
    """
    The request is authenticated as an admin to create update delete, or is a authenticated read-only request.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and request.user and request.user.is_authenticated:
            return True

        if request.user and request.user.is_authenticated and request.user.is_admin:
            return True

        return False
