from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class FrontProfile(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)