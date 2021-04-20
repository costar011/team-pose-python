from os import name
from django.db import models


class MemberModel(models.Model):
    """ Member Model Definition """

    name = models.CharField(max_length=30)
    birth = models.DateField()
    gender = models.CharField(max_length=10)
    avatar = models.ImageField()
    mobile = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True)
