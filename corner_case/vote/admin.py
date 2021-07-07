from django.contrib import admin

from corner_case.vote.models import Vote


@admin.register(Vote)
class RestaurantAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    list_display = (
        "id",
        "user",
        "menu",
        "date",
    )

    search_fields = ("name",)
    ordering = ("id", "user", "menu", "date")
    filter_horizontal = ()
