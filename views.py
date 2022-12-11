"""
Definition of views.
"""
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView, CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return render(
        request,
        'app/login_main.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
    else :
        return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'About page.',
            'year':datetime.now().year,
        }
    )

def registeruser(request):
    form_register = RegistrationForm()
    if request.method == "POST":
        form_register = RegistrationForm(request.POST)
        if form_register.is_valid():
            form_register.save()
            return redirect('login')

    context = {'form':form_register}

    return render(request, 'app/register.html', context)
    

