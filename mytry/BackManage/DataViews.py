from .models import *

class ShowUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=254)
    is_superuser = models.SmallIntegerField(default=0)
    is_staff = models.SmallIntegerField(default=0)

    class Meta:
        db_table = 'show_user'
        managed = False