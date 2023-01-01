from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def base_view(request):
    return render(request, 'base.html', {})


def homepage_view(request):
    return render(request, 'home.html', {})


def about_view(request):
	return render(request,'about.html', {})


def contact_view(request):
    return render(request,'contact.html', {})


def help_view(request):
    return render(request,'help.html', {})

