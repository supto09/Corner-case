from django.urls import path

from corner_case.restaurant.api.views import (
    RestaurantListCreateApiView,
    RestaurantRetrieveDestroyApiView,
    MenuListCreateApiView,
    MenuRetrieveApiView,
    MenuTodayListApiView,
)

app_name = "restaurants"
urlpatterns = [
    path("", RestaurantListCreateApiView.as_view()),
    path("/<int:id>", RestaurantRetrieveDestroyApiView.as_view()),
    path("/menu", MenuListCreateApiView.as_view()),
    path("/menu/today", MenuTodayListApiView.as_view()),
    path("/menu/<int:id>", MenuRetrieveApiView.as_view()),
]
