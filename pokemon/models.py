from django.db import models


class Species(models.Model):
    name = models.CharField(max_length=400, unique=True)

    def __str__(self):
        return self.name



class Ability(models.Model):
    name = models.CharField(max_length=400, unique=True)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=400, unique=True)
    height = models.IntegerField(null=True)
    base_experience = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    species = models.ForeignKey(Species, null=True, on_delete=models.SET_NULL)
    abilities = models.ManyToManyField(Ability)

    def __str__(self):
        return f"Pokemon named {self.name}, {self.height} tall, weighing {self.weight}, " \
               f"of species {self.species}"



