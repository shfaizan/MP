from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    
    return render(request, "home_page.html", {})

def contact(request):
    return render(request, "home_page.html", {})

def price(request):
    return render(request, "home_page.html", {})

def about(request):
    return render(request, "home_page.html", {})