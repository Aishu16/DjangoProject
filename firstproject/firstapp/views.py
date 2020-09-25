from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'firstapp/home.html')

def about(request):
    return HttpResponse("About Page")

def contact(request):
    return HttpResponse("Contact us")
