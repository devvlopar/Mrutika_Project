from django.urls import path
from myapp.views import *

urlpatterns = [
    path('mrutika/', fun1, name = 'mrutika'),
    path('', index, name = 'index'),
    path('beauty/', beauty, name = 'beauty'),
    path('contact/', contact, name = 'contact'),
    path('fashion/', fashion, name = 'fashion'),
    path('register/', register, name = 'register'),


]