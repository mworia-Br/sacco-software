from django.db import models
from django.contrib.auth.models import AbstractUser

class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    membership_number = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=20)
    pin = models.CharField(max_length=4)

class Account(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=10, unique=True)
    account_type = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class Loan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_number = models.CharField(max_length=10, unique=True)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    term = models.IntegerField()
    status = models.CharField(max_length=20)

class Savings(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    savings_amount = models.DecimalField(max_digits=10, decimal_places=2)
    savings_date = models.DateField()

class Teller(AbstractUser):
    employee_id = models.CharField(max_length=10, unique=True)
    is_teller = models.BooleanField(default=False)

class Agent(AbstractUser):
    agent_id = models.CharField(max_length=10, unique=True)
    is_agent = models.BooleanField(default=False)

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    teller = models.ForeignKey(Teller, on_delete=models.SET_NULL, null=True, blank=True)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_type = models.CharField(max_length=20)
    remarks = models.TextField(max_length=255, blank=True)

    