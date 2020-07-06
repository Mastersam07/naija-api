
from django.db import models


class State(models.Model):
    name = models.CharField(max_length=20)
    capital = models.CharField(max_length=20)
    slug = models.SlugField(max_length=21)

    def __str__(self):
        return self.name


class LocalGovernmentArea(models.Model):
    state = models.ForeignKey(
        State, on_delete=models.SET_NULL, null=True, related_name='lgas')
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
