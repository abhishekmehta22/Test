from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "home1.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")
                

def blog(request):
    return render(request, "blog.html")