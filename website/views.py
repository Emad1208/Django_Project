from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index_view(request):
    return HttpResponse('<h1>Home Page Project</h1>')



def about_view(request):
    return HttpResponse('<h1>About Us</h1>')



def contact_view(request):
    return HttpResponse('<h1>Contact Us</h1>')