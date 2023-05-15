from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fun1(request):
    # HttpResponse
    return HttpResponse('hello') # ye string browser pe show karega

def index(request):
    return render(request, 'index.html')
    

def beauty(request):
    return render(request, 'beauty.html')


def contact(request):
    return render(request, 'contact.html')


def fashion(request):
    return render(request, 'fashion.html')



def register(request):
    # rlsqtqmvajrwjrkn
    # mrutika96@gmail.com
    return render(request, 'register.html')

