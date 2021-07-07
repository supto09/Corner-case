from rest_framework import serializers

from corner_case.restaurant.api.serializers import MenuSerializer
from corner_case.restaurant.models import Menu
from corner_case.users.api.serializers import UserSerializer
from corner_case.vote.models import Vote


class VoteCreateSerializer(serializers.ModelSerializer):
    menu_id = serializers.IntegerField(write_only=True)

    menu = MenuSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Vote
        fields = ["menu_id", "menu", "user", "date"]
        read_only_fields = ["menu", "user", "date"]

    # validate if menu is created
    def validate_menu_id(self, value):
        if not Menu.objects.filter(id=value).exists():
            raise serializers.ValidationError("No menu found given menu id")

        return value

    # validate if user has already voted for the same day of menu in concern
    def validate(self, attrs):
        user = self.context["request"].user

        # we can check this way because every vote day will be saved with menus day
        menu_id = attrs["menu_id"]
        menu = Menu.objects.get(id=menu_id)

        if Vote.objects.filter(user=user, menu=menu).exists():
            raise serializers.ValidationError("Already voted on this menu")

        if Vote.objects.filter(user=user, date=menu.date).exists():
            raise serializers.ValidationError(
                "Already voted on another menu for same day"
            )

        return attrs

    def create(self, validated_data):
        user = self.context["request"].user
        menu_id = validated_data["menu_id"]
        menu = Menu.objects.get(id=menu_id)

        vote_instance = Vote.objects.create(user=user, menu=menu, date=menu.date)
        return vote_instance
