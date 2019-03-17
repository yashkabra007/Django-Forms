from django import forms
from .models import ContactForm, User
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


class ContactForms(forms.ModelForm):

    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'subject', 'message')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'gender')

