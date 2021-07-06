from rest_framework import serializers

from corner_case.restaurant.models import Restaurant, Menu


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    restaurant_id = serializers.IntegerField(write_only=True)
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = "__all__"

        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Menu.objects.all(),
        #         fields=("restaurant_id", "date"),
        #         message="There is an existing menu for the same date"
        #     )
        # ]

    def validate_restaurant_id(self, value):
        if not Restaurant.objects.filter(id=value).exists():
            raise serializers.ValidationError("No restaurant found with given restaurant id")

        return value

    def validate(self, attrs):
        restaurant_id = attrs['restaurant_id']
        date = attrs['date']

        if Menu.objects.filter(restaurant_id=restaurant_id, date=date).exists():
            raise serializers.ValidationError("There is an existing menu for the same date")

        return attrs
