from django.urls import path

from corner_case.users.api.views import ObtainAuthToken

app_name = "users"
urlpatterns = [
    path('', ObtainAuthToken.as_view()),
]
