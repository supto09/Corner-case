from django.contrib.auth import authenticate
from rest_framework import serializers

from corner_case.users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, write_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "type", "password"]
        read_only_fields = ["id"]
        extra_kwargs = {"type": {"required": True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()

        if self.validated_data["type"] == User.Types.ADMIN:
            user.admin = True

        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Email")
    password = serializers.CharField(
        label="Password", style={"input_type": "password"}, trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        print("Email", email)
        print("Password", password)

        if email and password:
            user = authenticate(
                request=self.context.get("request"), email=email, password=password
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            print("authenticate", user)
            if not user:
                raise serializers.ValidationError(
                    "Unable to log in with provided credentials.", code="authorization"
                )
        else:
            raise serializers.ValidationError(
                'Must include "username" and "password".', code="authorization"
            )

        attrs["user"] = user
        return attrs
