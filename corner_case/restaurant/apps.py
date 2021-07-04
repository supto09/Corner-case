from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "corner_case.restaurant"
    verbose_name = _("Restaurants")

    def ready(self):
        try:
            import corner_case.restaurant.signals  # noqa F401
        except ImportError:
            pass
