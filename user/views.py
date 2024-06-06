from .models import Vendor, VendorApplication, VendorVerification, Customer, SecurityQuestion
from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import SignupForm, CustomerForm, VendorApplicationForm, VendorVerificationForm, SecurityQuestionForm, VendorForm, SQForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import random
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model
from django.db.models import Q

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
                # if SecurityQuestion.DoesNotExist:
                #     print('not')
                #     return redirect('security_questions')
                # else:
                #     print('done')
                #     return redirect('vendor_profile')
            else:
                messages.info(request, 'Username or password is incorrect') 

        context = {}
        return render (request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('logout')
    success_message = 'Your Password has been changed successfully'    
    
        
# @login_required(login_url='login')
def set_security_questions(request):
    
    try:
        security_question = SecurityQuestion.objects.get(username=request.user.customer)
    except SecurityQuestion.DoesNotExist:
        security_question = None
    
    form = SQForm(instance=security_question)
    if request.method == 'POST':
        form = SQForm(request.POST, instance=security_question)
        if form.is_valid():
            security_question = form.save(commit=False)
            security_question.username = request.user.customer
            security_question.save()
            return redirect('customer_profile')

    context = {'form':form}

    return render(request, 'registration/set_security_questions.html', context)


User = get_user_model()
def reset_password(request):
    if request.method == 'POST':
        form = SecurityQuestionForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            answer2 = request.POST.get('answer2')


            user = User.objects.filter(Q(username=username) | Q(email=username)).first()

            if user:
                security_question = user.customer.securityquestion
                if (security_question.answer2 == answer2):
                    request.session['reset_user_id'] = user.id
                    print(user)
                    login(request, user)
                    return redirect('set_new_password')
                else:
                    print('not')
                    messages.info(request, 'Incorrect Answer') 
            else:
                messages.info(request, "User not found")
    else:
        form = SecurityQuestionForm()
    return render(request, 'registration/reset_password.html', {'form':form})

def set_new_password(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('logout')
    else:
        form = SetPasswordForm(request.user)

    return render(request, 'registration/set_new_password.html', {'form':form})

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'

@login_required(login_url='login')
def customerProfile(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.info(request, 'Please fill the form')
    context = {'form': form}

    return render(request, 'customer/customer_profile.html', context)

@login_required(login_url='login')
def customerBase(request):
    return render(request, 'customer/customer.html')

@login_required(login_url='login')
# @allowed_users(allowed_roles=['vendor'])
def vendor(request):
    context = {}
    return render(request, 'vendor/vendor.html', context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['vendor'])
def vendorProfile(request):
    vendor = request.user.vendor
    form = VendorForm(instance=vendor)
    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES, instance=vendor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.info(request, 'Please fill the form')
    context = {'form': form}
    return render (request, 'vendor/vendor_profile.html', context)


@login_required(login_url='login')
def vendorDetail(request, pk):
    vendor  = Vendor.objects.get(id=pk)
    context = {'vendor': vendor,}
    return render(request, 'vendor/vendor_detail.html', context)


@login_required(login_url='login')
def vendorApplication(request):
    if request.method == 'POST':
        form = VendorApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user

            application.save()
            messages.success(request, 'Application Submitted Successfully. Kindly keep an eye on your WhatsApp, SMS or Email for more informations within the next 24hrs')
            return redirect('customer_profile')
        
    else:
        form = VendorApplicationForm()


    context = {'form':form}
    return render(request, 'vendor/vendor_application.html', context)


@login_required(login_url='login')
def vendorVerification(request):
    if request.method == 'POST':
        form = VendorVerificationForm(request.POST, request.FILES)

        if form.is_valid():
            verification = form.save(commit=False)
            verification.user = request.user

            verification.save()
            messages.success(request, 'In Process')
            return redirect('customer_profile')
        
    else:
        form = VendorVerificationForm()

    context = {'form':form}
    return render(request, 'vendor/vendor_verification.html', context)