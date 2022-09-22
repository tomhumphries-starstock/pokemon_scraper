from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=400)
    description = models.CharField(max_length=600)

    def __str__(self):
        return self.name
