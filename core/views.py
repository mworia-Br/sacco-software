from django.shortcuts import render, redirect

# Create your views here.
from .models import Member, Account, Loan, Savings, Teller, Agent, Transaction

from django.contrib.auth.decorators import login_required

def register_member(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        membership_number = request.POST['membership_number']
        member = Member(first_name=first_name, last_name=last_name, email=email, membership_number=membership_number)
        member.save()
        return redirect('home')
    return render(request, 'register_member.html')

def apply_loan(request):
    if request.method == 'POST':
        member = Member.objects.get(pk=request.POST['member'])
        loan_amount = request.POST['loan_amount']
        interest_rate = request.POST['interest_rate']
        term = request.POST['term']
        loan = Loan(member=member, loan_amount=loan_amount, interest_rate=interest_rate, term=term, status='Pending')
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
        savings = Savings(member=member, savings_amount=savings_amount, savings_date=savings_date)
        savings.save()
        return redirect('home')
    members = Member.objects.all()
    return render(request, 'make_savings.html', {'members': members})

@login_required
def deposit(request):
    if request.method == 'POST':
        account = Account.objects.get(pk=request.POST['account'])
        amount = request.POST['amount']
        teller = Teller.objects.get(pk=request.POST['teller'])
        transaction = Transaction(account=account, amount=amount, teller=teller, transaction_type='Deposit')
        transaction.save()
        account.balance += amount
        account.save()
        return redirect('home')
    accounts = Account.objects.all()
    tellers = Teller.objects.all()
    return render(request, 'deposit.html', {'accounts': accounts, 'tellers': tellers})

@login_required
def withdrawal(request):
    if request.method == 'POST':
        account = Account.objects.get(pk=request.POST['account'])
        amount = request.POST['amount']
        agent = Agent.objects.get(pk=request.POST['agent'])
        transaction = Transaction(account=account, amount=amount, agent=agent, transaction_type='Withdrawal')

