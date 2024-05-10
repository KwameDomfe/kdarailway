from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import (redirect, render)
from django.urls import reverse

def accounts_layout (request):

    
    context = {
       
        }

    return render(request, 'accounts/accounts_layout.html', context)

def login_view (request):

    if request.method == "POST":
        
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect ('/')
    else:
        form = AuthenticationForm(request)
        
    context = {
         'form' : form
         }

    return render(request, 'accounts/login.html', context)

def logout_view(request):
    
    if request.method == 'POST':
        logout(request)
        return redirect('/accounts/login')
    
    context = {}

    return render(request, 'accounts/logout.html', context)

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/accounts/login')

    context={
        'form': form
    }

    return render(request, 'accounts/register.html', context)

