from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VotesConfig(AppConfig):
    name = "corner_case.vote"
    verbose_name = _("Votes")

    def ready(self):
        try:
            import corner_case.vote.signals  # noqa F401
        except ImportError:
            pass
