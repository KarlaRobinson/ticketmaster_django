from django.http import HttpResponse
def welcome(request):
	return HttpResponse("Hello World!")


# from django.views.decorators.csrf import ensure_csrf_cookie
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
	tickets_index = Ticket.objects.filter(agente__id='1')
	agente = Agente.objects.get(id="1").agente_email
	return render_to_response("ticketmaster/tickets.html",
							   {"tickets" : tickets_index,
							   "agente" : agente})

def ventas(request,):
	tickets_index = Ticket.objects.filter(ticket_estado='abierto')
	return render_to_response("ticketmaster/ventas.html",
							   {"tickets" : tickets_index})

# @ensure_csrf_cookie
def new_ticket(request, ):
	num = request.POST.get("num", "")
	a_id = request.POST.get("id", "")
	for i in range(int(num)):
		t = Ticket(ticket_estado='abierto', agente_id=int(a_id))
		t.save()
	agentes_index = Agente.objects.all()
	# for i in range(int(num)):
	# 	t = Ticket(ticket_estado='abierto', agente_id=int(id))
	# 	t.save()
	return render_to_response("ticketmaster/agentes.html",
							   {"agentes" : agentes_index})

def estado(request, ):
	estado = request.POST.get("estado", "")
	t_id = request.POST.get("id", "")
	t = Ticket.objects.get(id=t_id)
	t.ticket_estado = estado
	t.save()
	tickets_index = Ticket.objects.filter(agente__id='1')
	agente = Agente.objects.get(id="1").agente_email
	return render_to_response("ticketmaster/tickets.html",
							   {"tickets" : tickets_index,
							   "agente" : agente})




