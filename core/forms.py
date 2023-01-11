from django import forms

class MemberRegistrationForm(forms.Form):
first_name = forms.CharField(max_length=30)
last_name = forms.CharField(max_length=30)
email = forms.EmailField()
phone_number = forms.CharField(max_length=30)
membership_number = forms.CharField(max_length=10, unique=True)
pin = forms.CharField(max_length=10, widget=forms.PasswordInput)

class AccountCreationForm(forms.Form):
account_number = forms.CharField(max_length=10, unique=True)
account_type = forms.CharField(max_length=20)
pin = forms.CharField(max_length=10, widget=forms.PasswordInput)

class LoanApplicationForm(forms.Form):
member = forms.CharField(max_length=30)
loan_amount = forms.DecimalField(max_digits=10, decimal_places=2)
interest_rate = forms.DecimalField(max_digits=5, decimal_places=2)
term = forms.IntegerField()

class DepositForm(forms.Form):
account = forms.CharField(max_length=30)
amount = forms.DecimalField(max_digits=10, decimal_places=2)
pin = forms.CharField(max_length=10, widget=forms.PasswordInput)

class WithdrawalForm(forms.Form):
account = forms.CharField(max_length=30)
amount = forms.DecimalField(max_digits=10, decimal_places=2)
pin = forms.CharField(max_length=10, widget=forms.PasswordInput)

class LoginForm(forms.Form):
username = forms.CharField(max_length=30)
password = forms.CharField(max_length=30, widget=forms.PasswordInput)

class SavingsForm(forms.Form):
member = forms.CharField(max_length=30)
savings_amount = forms.DecimalField(max_digits=10, decimal_places=2)
savings_date = forms.DateField()