from django.urls import path
from myapp.views import *

urlpatterns = [
    path('mrutika/', fun1, name = 'mrutika'),
    path('', index, name = 'index'),
    path('beauty/', beauty, name = 'beauty'),
    path('contact/', contact, name = 'contact'),
    path('fashion/', fashion, name = 'fashion'),
    path('register/', register, name = 'register'),
    path('create_user/', create_user, name = 'create_user'),
    path('otp/', otp, name = 'otp'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),






]
