from django.shortcuts import render, redirect

# Create your views here.
from .models import Member, Account, Loan, Savings

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