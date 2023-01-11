from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Member(AbstractUser):
    membership_number = models.CharField(max_length=10, unique=True)
    pin = models.CharField(max_length=4, blank=True)

class Teller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    employee_id = models.CharField(max_length=10, unique=True)

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    agent_id = models.CharField(max_length=10, unique=True)