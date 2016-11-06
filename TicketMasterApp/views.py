from django.shortcuts import render

from django.http import HttpResponse
def welcome(request):
    return HttpResponse("Hello World!")

from django.shortcuts import render_to_response
def tester(request,):
    return render_to_response("agentes/home.html",
                               {"Testing" : "Django Template Inheritance ",
                              "HelloHello" : "Hello World - Django"})

def home(request,):
    return render_to_response("ticketmaster/home.html")

def login(request,):
    return render_to_response("ticketmaster/login.html")

def agentes(request,):
    return render_to_response("ticketmaster/agentes.html",
                               {"Testing" : "Django Template Inheritance ",
                              "HelloHello" : "Hello World - Django"})

def tickets(request,):
    return render_to_response("ticketmaster/tickets.html")

def ventas(request,):
    return render_to_response("ticketmaster/ventas.html")