from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context ={
        "title": "helloo"
    }
    return render(request, "home_page.html", context)

def contact(request):
    return render(request, "contact/view.html", {})

def price(request):
    return render(request, "home_page.html", {})

def about(request):
    return render(request, "home_page.html", {})