from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Member, Account, Loan, Savings, Teller, Agent, Transaction


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def deposit(request):
    if request.method == 'POST':
        account = Account.objects.get(pk=request.POST['account'])
        amount = request.POST['amount']
        pin = request.POST['pin']
        if account.member.pin == pin:
            transaction = Transaction(
                account=account, amount=amount, transaction_type='Deposit')
            transaction.save()
            account.balance += amount
            account.save()
            return redirect('home')
        else:
            return redirect('deposit')
    accounts = Account.objects.all()
    return render(request, 'deposit.html', {'accounts': accounts})


@user_passes_test(lambda u: u.is_teller)
def withdrawal(request):
    if request.method == 'POST':
        account = Account.objects.get(pk=request.POST['account'])
        amount = request.POST['amount']
        pin = request.POST['pin']
        if account.member.pin == pin:
            transaction = Transaction(
                account=account, amount=amount, transaction_type='Withdrawal')
            transaction.save()
            account.balance -= amount
            account.save()
            return redirect('home')
        else:
            return redirect('withdrawal')
    accounts = Account.objects.all


def register_member(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        membership_number = request.POST['membership_number']
        member = Member(first_name=first_name, last_name=last_name,
                        email=email, membership_number=membership_number)
        member.save()
        return redirect('home')
    return render(request, 'register_member.html')


def apply_loan(request):
    if request.method == 'POST':
        member = Member.objects.get(pk=request.POST['member'])
        loan_amount = request.POST['loan_amount']
        interest_rate = request.POST['interest_rate']
        term = request.POST['term']
        loan = Loan(member=member, loan_amount=loan_amount,
                    interest_rate=interest_rate, term=term, status='Pending')
        loan.save()
        return redirect('home')
    members = Member.objects.all()
    return render(request, 'apply_loan.html', {'members': members})


def approve_loan(request, loan_id):
    loan = Loan.objects.get(pk=loan_id)
    loan.status = 'Approved'
    loan.save()
    return redirect('home')


def view_members(request):
    members = Member.objects.all()
    return render(request, 'view_members.html', {'members': members})


def view_accounts(request, member_id):
    member = Member.objects.get(pk=member_id)
    accounts = Account.objects.filter(member=member)
    return render(request, 'view_accounts.html', {'accounts': accounts})


def make_savings(request):
    if request.method == 'POST':
        member = Member.objects.get(pk=request.POST['member'])
        savings_amount = request.POST['savings_amount']
        savings_date = request.POST['savings_date']
        savings = Savings(
            member=member, savings_amount=savings_amount, savings_date=savings_date)
        savings.save()
        return redirect('home')
    members = Member.objects.all()
    return render(request, 'make_savings.html', {'members': members})


def make_savings_withdrawal(request):
    if request.method == 'POST':
        member = Member.objects.get(pk=request.POST['member'])
        savings = Savings.objects.get(member=member)
        account = Account.objects.get(pk=request.POST['account'])
        amount = request.POST['amount']
        pin = request.POST['pin']
        if savings.savings_amount >= amount and account.member.pin == pin:
            savings.savings_amount -= amount
            savings.save()
            transaction = Transaction(account=account, amount=amount,
                          transaction_type='Savings Withdrawal')
            transaction.save()
            account.balance += amount
            account.save()
            return redirect('home')
        else:
            return redirect('savings_withdrawal')
    members = Member.objects.all()
    accounts = Account.objects.filter(member=member)
    return render(request, 'savings_withdrawal.html', {'members': members, 'accounts': accounts})


def make_savings_deposit(request):
    if request.method == 'POST':
        member = Member.objects.get(pk=request.POST['member'])
        savings = Savings.objects.get(member=member)
        account = Account.objects.get(pk=request.POST['account'])
        amount = request.POST['amount']
        pin = request.POST['pin']
    if account.balance >= amount and account.member.pin == pin:
        savings.savings_amount += amount
        savings.save()
        transaction = Transaction(account=account, amount=amount,
                          transaction_type='Savings Deposit')
        transaction.save()
        account.balance -= amount
        account.save()
        return redirect('home')
    else:
        return redirect('savings_deposit')
    members = Member.objects.all()
    accounts = Account.objects.filter(member=member)
    return render(request, 'savings_deposit.html', {'members': members, 'accounts': accounts})
