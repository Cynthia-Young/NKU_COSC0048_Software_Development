
from django.db import models

# Create your models here.
from django.db import models

class HardwareInfo(models.Model):
    date = models.DateField()
    process_total = models.IntegerField()
    cpu_status = models.FloatField(max_length=20)
    memory_status = models.FloatField(max_length=20)
    gpu_status = models.FloatField(max_length=20)