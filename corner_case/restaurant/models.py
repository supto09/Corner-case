from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    date = models.DateField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["restaurant_id", "date"], name="same_day_menu"
            )
        ]

    def __str__(self):
        return str(self.id) + "=>" + self.name
