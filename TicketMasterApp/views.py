from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def welcome(request):
    return HttpResponse("Hello World!")
def bye(request):
    return HttpResponse("Good Bye World!")