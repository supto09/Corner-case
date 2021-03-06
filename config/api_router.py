from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path("users", include("corner_case.users.api.urls")),
    path("restaurants", include("corner_case.restaurant.api.urls")),
    path("votes", include("corner_case.vote.api.urls")),
]
