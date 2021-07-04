from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as an admin, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.is_admin
        )


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
