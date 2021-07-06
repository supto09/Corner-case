from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from drf_spectacular.utils import extend_schema_view, extend_schema

from corner_case.restaurant.api.serializers import RestaurantSerializer, MenuSerializer
from corner_case.restaurant.models import Restaurant, Menu
from corner_case.utils.permission_helper import IsAdminOrAuthenticatedReadOnly


@extend_schema_view(
    get=extend_schema(summary="List", ),
    post=extend_schema(summary="Create", description="Admin authorized only"),
)
class RestaurantListCreateApiView(ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrAuthenticatedReadOnly,)
    serializer_class = RestaurantSerializer

    queryset = Restaurant.objects.all()


@extend_schema_view(
    get=extend_schema(summary="Retrieve", ),
    put=extend_schema(summary="Update", description="Admin authorized only"),
    patch=extend_schema(summary="Partial Update", description="Admin authorized only"),
    delete=extend_schema(summary="Delete", description="Admin authorized only"),
)
class RestaurantRetrieveDestroyApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrAuthenticatedReadOnly,)
    serializer_class = RestaurantSerializer

    queryset = Restaurant.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "id"


@extend_schema_view(
    get=extend_schema(summary="List Menu", ),
    post=extend_schema(summary="Create Menu", description="Admin authorized only"),
)
class MenuListCreateApiView(ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrAuthenticatedReadOnly,)
    serializer_class = MenuSerializer

    queryset = Menu.objects.all()


@extend_schema_view(
    get=extend_schema(summary="Menu retrieve"),
)
class MenuRetrieveApiView(RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrAuthenticatedReadOnly,)
    serializer_class = MenuSerializer

    queryset = Menu.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "id"
