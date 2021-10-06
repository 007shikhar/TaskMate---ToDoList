from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.contrib.auth.models import User


class CustomRegisterForm(UserCreationForm):

    email = forms.EmailField(required=False)    #default -> required=True
    # firstname =forms.CharField(max_length=30)
    # lastname = forms.CharField(max_length=30, required=False)

    class Meta:

        model=User 

        fields=['username','email','password1','password2']