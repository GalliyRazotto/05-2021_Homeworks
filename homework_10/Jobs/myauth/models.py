from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.


class MyUser(AbstractUser):
    age = models.SmallIntegerField(default=18)
    email = models.EmailField(unique=True)

