from django.urls import path

from corner_case.users.api.views import ObtainAuthToken, CreateUserView

app_name = "users"
urlpatterns = [
    path('/login', ObtainAuthToken.as_view()),
    path('/create', CreateUserView.as_view()),
]
