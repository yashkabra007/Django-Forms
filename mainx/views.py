from django.shortcuts import render
from .forms import ContactForms, SignUpForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'index.html')


def contact_form(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('/mainx/')
    else:
        form = ContactForms()
        return render(request, 'contact.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/mainx/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

