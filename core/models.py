# models.py
from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    membership_number = models.CharField(max_length=10, unique=True)

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