from django.urls import path

from corner_case.users.api.views import LoginView, CreateUserView, LogoutView

app_name = "users"
urlpatterns = [
    path("/login", LoginView.as_view()),
    path("/logout", LogoutView.as_view()),
    path("/create", CreateUserView.as_view()),
]
