from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
class SumModel(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
# Create your models here.
