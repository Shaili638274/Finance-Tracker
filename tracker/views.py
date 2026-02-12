from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from .models import Transaction
from .forms import TransactionForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)

    income = sum(t.amount for t in transactions if t.transaction_type == 'Income')
    expense = sum(t.amount for t in transactions if t.transaction_type == 'Expense')
    balance = income - expense

    return render(request, 'dashboard.html', {
        'transactions': transactions,
        'income': income,
        'expense': expense,
        'balance': balance
    })

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def benefits(request):
    return render(request, 'benefits.html')