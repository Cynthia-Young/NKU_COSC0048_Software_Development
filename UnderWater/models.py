from django.db import models

class Fish(models.Model):
    Species=models.CharField(max_length=30)
    Weight= models.FloatField(help_text="单位：g")
    Length1=models.FloatField(help_text="单位：cm")
    Length2=models.FloatField(help_text="单位：cm")
    Length3=models.FloatField(help_text="单位：cm")
    Height= models.FloatField(help_text="单位：cm")
    Width= models.FloatField(help_text="单位：cm")
