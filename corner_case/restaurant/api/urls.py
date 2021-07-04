from django.urls import path

from corner_case.restaurant.api.views import RestaurantListCreateApiView, RestaurantRetrieveDestroyApiView

app_name = "restaurants"
urlpatterns = [
    path('', RestaurantListCreateApiView.as_view()),
    path('/<int:id>', RestaurantRetrieveDestroyApiView.as_view()),
]
