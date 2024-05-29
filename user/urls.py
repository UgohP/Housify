from re import template
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)


urlpatterns = [
    path('signup/', signupPage, name='signup'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    # path('customer/', customerBase, name='customer'),
    # path('customer_profile/', customerProfile, name='customer_profile'),
    # path('vendor_profile/', vendorProfile, name='vendor_profile'),
    # path('vendor/', vendor, name='vendor'),
    # path('vendor_application/', vendorApplication, name='vendor_application'),
    # path('vendor_verification/', vendorVerification, name='verifying'),
    # path('vendor_detail/<int:pk>/', vendorDetail, name='vendor_detail'),
    # path('change_password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'), name='change_password' ),
    # path('reset_password/', reset_password, name="reset_password"),
    # path('set_new_password/', set_new_password, name="set_new_password"),
    # path('security_questions/', set_security_questions, name="security_questions"),
]