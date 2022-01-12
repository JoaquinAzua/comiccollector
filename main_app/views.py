from django import http
from django.http.response import HttpResponse
from django.shortcuts import render



# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def comics_index(request):
    return render(request, 'comics/index.html')