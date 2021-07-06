from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from corner_case.vote.api.serializers import VoteCreateSerializer
from corner_case.vote.models import Vote


@extend_schema_view(
    post=extend_schema(summary="Vote for menu"),
)
class VoteCreateApiView(CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = VoteCreateSerializer
    queryset = Vote.objects.all()
