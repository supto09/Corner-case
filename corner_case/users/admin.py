from django.contrib import admin
from django.contrib.auth.models import Group

from corner_case.users.forms import UserCreationForm, UserChangeForm
from corner_case.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("email", "type")
    list_filter = ("type",)

    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.form = UserChangeForm
        else:
            self.form = UserCreationForm
        return super(UserAdmin, self).get_form(request, obj, **kwargs)


# Remove Group Model and Site from admin. We're not using it.
admin.site.unregister(Group)
