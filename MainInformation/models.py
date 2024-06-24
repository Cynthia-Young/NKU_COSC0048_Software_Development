from django.db import models

# Create your models here.
from django.db import models

class Water(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.CharField(max_length=30,unique=True)
    type = models.CharField(max_length=20)
    temperature = models.FloatField()
    ph = models.FloatField()
    dissolved_oxygen = models.FloatField(verbose_name="溶氧量", help_text="单位: mg/L")
    conductivity = models.FloatField(verbose_name="电导率", help_text="单位: μS/cm")
    turbidity = models.FloatField(verbose_name="浊度", help_text="单位: NTU")
    permanganate_index = models.FloatField(verbose_name="高锰酸盐指数", help_text="单位: mg/L")
    ammonia_nitrogen = models.FloatField(verbose_name="氨氮", help_text="单位: mg/L")
    total_phosphorus = models.FloatField(verbose_name="总磷", help_text="单位: mg/L")
    total_nitrogen = models.FloatField(verbose_name="总氮", help_text="单位: mg/L")

    def __str__(self):
        return f"Water sample #{self.id} at {self.time}"
