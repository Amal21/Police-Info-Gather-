from django.db import models


class Recherche(models.Model):
    cin = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    


class User(models.Model):
    pass


