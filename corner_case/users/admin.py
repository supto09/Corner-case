from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from corner_case.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'type')
    list_filter = ('type',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('admin',)}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Remove Group Model and Site from admin. We're not using it.
admin.site.unregister(Group)
