from django import forms

from corner_case.users.models import User


class UserCreationForm(forms.ModelForm):
    """
    A form for creating new User. Includes all the required
    fields, plus a repeated password.
    """

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("email", "type")

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)

        # Save the provided password in hashed format
        user.set_password(self.cleaned_data["password1"])

        if self.cleaned_data["type"] == User.Types.ADMIN:
            user.admin = True

        if commit:
            user.save()

        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users."""

    class Meta:
        model = User
        fields = (
            "email",
            "type",
        )

    def save(self, commit=True):
        user = super(UserChangeForm, self).save(commit=False)

        if self.cleaned_data["type"] == User.Types.ADMIN:
            user.admin = True

        if commit:
            user.save()

        return user
