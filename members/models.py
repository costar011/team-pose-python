from os import name
from django.db import models


class MemberModel(models.Model):
    """ Member Model Definition """

    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"
    GENDER_OTHER = "Other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    name = models.CharField(max_length=30)
    birth = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    avatar = models.ImageField()
    mobile = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True)

    # slef :  나 자신
    def __str__(self):
        return self.name
