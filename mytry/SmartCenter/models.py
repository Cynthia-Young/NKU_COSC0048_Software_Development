
from django.db import models

# Create your models here.
class EnvironmentData(models.Model):
    monitoring_date = models.DateField()
    water_quality = models.CharField(max_length=10)
    water_temperature = models.FloatField()
    ph_level = models.FloatField()
    dissolved_oxygen = models.FloatField()

    class Meta:
        ordering = ['monitoring_date']

class Fish_detect(models.Model):
    code = models.CharField(max_length=10, unique=True)
    species = models.CharField(max_length=50)
    length = models.FloatField()
    weight = models.IntegerField()

    def __str__(self):
        return self.species

