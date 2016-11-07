

from django.http import HttpResponse
def welcome(request):
    return HttpResponse("Hello World!")

from django.shortcuts import render_to_response
from TicketMasterApp.models import Supervisor, Agente, Ticket
# def tester(request,):
#     return render_to_response("agentes/home.html",
#                                {"Testing" : "Django Template Inheritance ",
#                               "HelloHello" : "Hello World - Django"})

def home(request,):
    return render_to_response("ticketmaster/home.html")

def login(request,):
    return render_to_response("ticketmaster/login.html")

def agentes(request,):
	agentes_index = Agente.objects.all()
	return render_to_response("ticketmaster/agentes.html",
                               {"agentes" : agentes_index})

def tickets(request,):
	tickets_index = Ticket.objects.all()
	agente = Agente.objects.get(id="1").agente_email
	return render_to_response("ticketmaster/tickets.html",
                               {"tickets" : tickets_index,
                               "agente" : agente})

def ventas(request,):
	tickets_index = Ticket.objects.all()
	return render_to_response("ticketmaster/ventas.html",
                               {"tickets" : tickets_index})

def new_ticket(request,):
    t = Ticket(ticket_estado='a')
    t.save()
    return render_to_response("ticketmaster/tickets.html")

def pendiente():
	t = Ticket.objects.get(id=1)
	t.ticket_estado = 'p'
	t.save()
	return render_to_response("ticketmaster/tickets.html")

def cerrado():
	t = Ticket.objects.get(id=1)
	t.ticket_estado = 'c'
	t.save()
	return render_to_response("ticketmaster/tickets.html")




