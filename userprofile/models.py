
from django.contrib.auth.models import AbstractUser, User
from django.db import models


class UserProfile(AbstractUser):
    avatar = models.ImageField(upload_to="avatar/%Y%m%d/", default="avatar/20210705/default.png", blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.username
