from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=255)
    dictionary = models.CharField(max_length=255)

    def __str__(self):
        return self.name