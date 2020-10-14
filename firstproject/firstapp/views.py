from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def home(request):
    return render(request, 'firstapp/home.html')

def about(request):
    return HttpResponse("About Page")

def contact(request):
    return HttpResponse("Contact us")

def form_view(request):
    if request.method=='POST':
        form=forms.Registerform(request.POST)
        if form.is_valid():
            print("validation worked")
            print("Name : " + form.cleaned_data['name'])
            print("Email_id : " + form.cleaned_data['email'])
            print("Text : " + form.cleaned_data['text'])


    form = forms.Registerform
    return render(request, 'firstapp/register.html', {'form':form})

