# from .forms import UserRegistration
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact_us, Sign_up
from django.contrib.auth.models import User, auth


# Create your views here.
def home(request):
    return render(request, "home1.html")


def about(request):
    return render(request, "about.html")
                

def blog(request):
    return render(request, "blog.html")


def sign_up(request):
    if request.method == "POST":
        first_nm = request.POST['first_name']
        last_nm = request.POST['last_name']
        usernm = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password1']
        cpwd = request.POST['password2']

        ins = Sign_up(first_name=first_nm, last_name=last_nm, username=usernm, email=email, password=pwd)
        ins.save
        print("created user")
        return redirect('about.html')
    else:
        return render(request, "home1.html")


# def login(request):
#     if request.method == "POST":
#         uname = request.POST['user']
#     return render()

def contact(request):
    
    if request.method == "POST":
        print("hello")
        nm = request.POST['name']
        em = request.POST['email']
        mbl = request.POST['mobile']
        mssg = request.POST['message']
        ins = Contact_us(name=nm, email=em, mobile=mbl, msg=mssg)
        ins.save()
        print("data successfully entered to db")
        # form = UserRegistration(request.POST)
        # if form.is_valid():
        #     form.save()
        #     nm = form.cleaned_data['name']
        #     em = form.cleaned_data['email']
        #     mbl = form.cleaned_data['mobile']
        #     mssg = form.cleaned_data['msg']
        #     all_ = Contact_us(name=nm, email=em, mobile=mbl, msg=mssg)
        #     all.save()
        #     form = UserRegistration()
        # else:
        #     form = UserRegistration()
        
    return render(request, 'contact.html')
            