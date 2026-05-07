from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Expense, BudgetCycle


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount']
        

class BudgetCycleForm(forms.ModelForm):
    class Meta:
        model = BudgetCycle
        fields = ['total_amount', 'start_date', 'end_date']
        

