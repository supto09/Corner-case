from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name
