from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail
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


def create_user(request):
    #request.POST = {'csrfmiddlewaretoken': ['WmQOCjI77dU4kOPRfQ8Q6Otke9DAsLVw39bnC0t4aAZxvZjJecJOBSDZvhHEk2LK'], 'fname': ['ashwini'], 'email': ['devang.tops@gmail.com'], 'passwd': ['123'], 'cpasswd': ['123']}
    try:
        u1 = User.objects.get(email = request.POST['email']) #ek row OBJ bana ke return karega
        return render(request, 'register.html', {'msg': 'email Already exists'})
    except:
        #error aaya matalab email new hai
        if request.POST['passwd'] == request.POST['cpasswd']:
            # send_mail()
            User.objects.create(
                full_name = request.POST['fname'],
                email = request.POST['email'],
                password = request.POST['passwd']
            )
            return render(request, 'register.html', {'msg': 'successfully created!!'})
        else:
            return render(request, 'register.html', {'msg': 'Passwords Do not Match'})
    
    # 
    # request.POST['fname']

