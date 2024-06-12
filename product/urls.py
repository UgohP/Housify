from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('fashion_categories/', fashionCategory, name='fashion_category'),
    # path('fashion/<fash_pro>', fashionProduct, name='fashion'),
    path('get_product/<str:pk>', getProduct, name='get_product'),
    path('create_product/', createProduct, name='create_product'),
    path('update_product/<int:pk>/', updateProduct, name='update_product'),
    path('delete_product/<int:pk>/', deleteProduct, name='delete_product'),
    path('history/', history, name='history'),

]