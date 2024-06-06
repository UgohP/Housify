from django.urls import path
from .views import homepage, categories
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', homepage, name='homepage'),
    # path('countdown/', countdown, name = 'countdown'),
    # path('', blue, name = 'bluemartin'),
    # path('homepage/', home, name = 'home'),
    path('categories/', categories, name='categories'),
    # path('terms_and_conditions/', TermsAndConditions, name='terms'),
]