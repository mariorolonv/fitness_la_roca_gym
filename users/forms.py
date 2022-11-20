from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegisterForm(UserCreationForm):
  
    class Meta():
        model = User
        fields = ['first_name','last_name','username','password1','password2','document_type','document_number']

class FormClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name','last_name','document_type','document_number']
        
class FormInvoice(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['client','payment_type','total','status','date_joined']
        widgets = {'date_joined': forms.DateInput(attrs={'type': 'date'})}
        
class FormEditInvoice(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['client','payment_type','total','status']