from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    return render(request,'LandingPage/landing_page.html')

def upload(request):
    return render(request,'LandingPage/uploads.html')

