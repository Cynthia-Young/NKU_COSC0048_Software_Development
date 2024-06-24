from django.db import models

# Create your models here.
class Device(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=200)
    description = models.TextField(null=True)
    state = models.SmallIntegerField(default=0)



