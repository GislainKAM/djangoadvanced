from msilib.schema import Verb
from pyexpat import model
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBCRIBER"

    ROLE_CHOICES = (
        (CREATOR, 'Createur'),
        (SUBSCRIBER, 'Abonne'),
        )
    profile_photo = models.ImageField(verbose_name="photo de profile")
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name="Role")


