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