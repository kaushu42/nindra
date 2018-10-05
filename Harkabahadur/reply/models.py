from django.db import models


class response(models.Model):
    name = models.CharField(max_length=200)
    values = models.CharField(max_length=200)


def __str__(self):
    return self.name + "- " + self.values