from django.contrib import admin

from corner_case.restaurant.models import Restaurant, Menu


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    list_display = ("id", "name")

    search_fields = ("name",)
    ordering = ("id", "name",)
    filter_horizontal = ()


@admin.register(Menu)
class RestaurantAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    list_display = ("id", "name", "date", "restaurant")

    search_fields = ("name",)
    ordering = ("id", "name", "date")
    filter_horizontal = ()
