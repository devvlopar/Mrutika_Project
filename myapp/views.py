from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail
import random
from django.conf import settings
# Create your views here.

def fun1(request):
    # HttpResponse
    return HttpResponse('hello') # ye string browser pe show karega

def index(request):
    try:
        u1 = User.objects.get(email = request.session['email'])
        return render(request, 'index.html', {'userdata': u1})
    except:
        return render(request, 'index.html')
    

def beauty(request):
    return render(request, 'beauty.html')


def contact(request):
    return render(request, 'contact.html')


def fashion(request):
    return render(request, 'fashion.html')



def register(request):
    # 
    # 
    return render(request, 'register.html')


def create_user(request):
    #request.POST = {'csrfmiddlewaretoken': ['WmQOCjI77dU4kOPRfQ8Q6Otke9DAsLVw39bnC0t4aAZxvZjJecJOBSDZvhHEk2LK'], 'fname': ['ashwini'], 'email': ['devang.tops@gmail.com'], 'passwd': ['123'], 'cpasswd': ['123']}
    try:
        u1 = User.objects.get(email = request.POST['email']) #ek row OBJ bana ke return karega
        return render(request, 'register.html', {'msg': 'email Already exists'})
    except:
        #error aaya matalab email new hai
        if request.POST['passwd'] == request.POST['cpasswd']:
            global c_otp
            c_otp = random.randint(1000, 9999)

            s = 'Welcome To Blog Website'
            m = f"Your OTP is {c_otp}"
            f_e = settings.EMAIL_HOST_USER
            r_l = [request.POST['email']]
            send_mail(s, m, f_e, r_l)
            global user_info
            user_info = [request.POST['fname'],
                         request.POST['email'], 
                         request.POST['passwd']]

            return render(request, 'otp.html')
            # User.objects.create(
            #     full_name = request.POST['fname'],
            #     email = request.POST['email'],
            #     password = request.POST['passwd']
            # )
            # return render(request, 'register.html', {'msg': 'successfully created!!'})
        else:
            return render(request, 'register.html', {'msg': 'Passwords Do not Match'})
    
    # 
    # request.POST['fname']



def otp(request):
    if c_otp == int(request.POST['u_otp']):
        User.objects.create(
            full_name = user_info[0],
            email = user_info[1],
            password = user_info[2]
        )
        return render(request, 'register.html', {'msg': 'successfully created'})
    else:
        return render(request, 'otp.html', {'msg': 'Invalid OTP'})
    

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            u1 = User.objects.get(email = request.POST['email'])
            if request.POST['passwd'] == u1.password:
                request.session['email'] = request.POST['email'] #iss line pe login ho gaya
                return redirect('index')
            else:
                return render(request, 'login.html', {'msg': 'Password is wrong'})
        except:
            return render(request, 'login.html', {'msg': 'Email Does Not Exist'})
        

def logout(request):
    del request.session['email']
    return redirect('index')