from django.db import models


# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=128)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    building_number = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    locality = models.CharField(max_length=512)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
