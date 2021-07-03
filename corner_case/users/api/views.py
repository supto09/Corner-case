from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.compat import coreapi, coreschema
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.views import APIView

from corner_case.users.api.serializers import UserSerializer, AuthTokenSerializer
from corner_case.users.models import User


class LoginView(APIView):
    serializer_class = AuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="Valid email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        token_serializer = self.get_serializer(data=request.data)
        token_serializer.is_valid(raise_exception=True)
        user = token_serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_serialized_data = UserSerializer(user, context={'request': request})
        return Response(
            {
                'token': token.key,
                'user': user_serialized_data.data
            }
        )


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'message': "User logged out successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({'message': "Invalid token provided"}, status=status.HTTP_401_UNAUTHORIZED)


class CreateUserView(CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
