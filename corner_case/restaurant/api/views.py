from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from corner_case.restaurant.api.serializers import RestaurantSerializer
from corner_case.utils.permission_helper import IsAdminOrAuthenticatedReadOnly


@extend_schema_view(
    get=extend_schema(summary="List", ),
    post=extend_schema(summary="Create", description="Admin authorized only"),
)
class RestaurantListCreateApiView(ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrAuthenticatedReadOnly,)
    serializer_class = RestaurantSerializer


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
