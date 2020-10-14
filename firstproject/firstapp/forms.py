from django import forms
from django.core import validators

class Registerform(forms.Form):
    name = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=40)
    text = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput, validators=[validators.MinLengthValidator(6, "Password should be atleast 6 characters")])




