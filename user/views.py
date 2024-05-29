from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import SignupForm, CustomerForm, VendorApplicationForm, VendorVerificationForm, SecurityQuestionForm, VendorForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from audioop import reverse
# from email.mime import application, message
# from itertools import product
# import random
# from ssl import create_default_context
# from django.shortcuts import render, redirect
# from .models import *
# from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm, AuthenticationForm, PasswordResetForm
# from django.contrib.auth.views import PasswordChangeView, PasswordResetView
# from django.contrib.auth.decorators import login_required
# from django.views.generic import ListView
# from django.views.generic.edit import *
# from django.urls import reverse_lazy
# from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib.auth import get_user_model
# from django.db.models import Q

# Create your views here.

def signupPage(request):
    """View for signup page"""
    
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = SignupForm()

        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')

                messages.success(request, 'Account was created for ' + user)
                return redirect('homepage')

        context = {'form': form}
        return render (request, 'registration/signup.html', context)
    
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
            #     if SecurityQuestion.DoesNotExist:
            #         print('not')
            #         return redirect('security_questions')
            #     else:
            #         print('done')
            #         return redirect('vendor_profile')
            else:
                messages.info(request, 'Username or password is incorrect') 

        context = {}
        return render (request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
