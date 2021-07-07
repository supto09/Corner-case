from django.db import models

from corner_case.restaurant.models import Menu
from corner_case.users.models import User


class Vote(models.Model):
    menu = models.ForeignKey(Menu, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    date = models.DateField(blank=False)

    # always save the menu's date to vote date
    def save(self, *args, **kwargs):
        self.date = self.menu.date
        super(Vote, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.email + " to " + self.menu.name
