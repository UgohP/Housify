from pyexpat import model
from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class SQForm(forms.ModelForm):
    class Meta:
        model = SecurityQuestion
        fields = ['username', 'question2', 'answer2']

class SecurityQuestionForm(forms.Form):
    username = forms.CharField(label="Enter Your Username or email", required=False)
    answer2 = forms.CharField(label='What is your favourite colour?')

class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['customer', 'is_vendor', 'in_process']

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        exclude = ['vendor']

class VendorApplicationForm(forms.ModelForm):
    class Meta:
        model = VendorApplication
        exclude = ['user']

class VendorVerificationForm(forms.ModelForm):
    class Meta:
        model = VendorVerification
        exclude = ['user']