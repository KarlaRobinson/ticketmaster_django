from django.http import HttpResponse

# from django.views.decorators.csrf import ensure_csrf_cookie

from django.shortcuts import render_to_response

from TicketMasterApp.models import Supervisor, Agente, Ticket

from django.core.exceptions import ObjectDoesNotExist

def home(request,):
	return render_to_response("ticketmaster/home.html")

def login(request,):
	return render_to_response("ticketmaster/login.html")

def auth_agente(request, email, password):
	try:
		agente = Agente.objects.get(agente_email=email)
		if agente:
			if agente.agente_password == password:
				request.session['id'] = agente.id
				request.session['type'] = "agente"
				return True
			else:
				return False
	except ObjectDoesNotExist:
		return False

def auth_supervisor(request, email, password):
	try:
		supervisor = Supervisor.objects.get(supervisor_email=email)
		if supervisor.supervisor_password == password:
			request.session['id'] = supervisor.id
			request.session['type'] = "supervisor"
			return True
		else:
			return False
	except ObjectDoesNotExist:
		return False

def logged_in(request,):
	try:
		type = request.session['type']
		return type
	except:
		return False

def agentes(request,):
	if logged_in(request) == "supervisor":
		agentes_index = Agente.objects.all()
		tickets = len(Agente.objects.get(id=1).ticket_set.all())
		return render_to_response("ticketmaster/agentes.html",
								   {"agentes" : agentes_index,
								   "tickets" : tickets})
	else:
		return render_to_response("ticketmaster/login.html")

def tickets(request,):
	email = request.POST.get("email", "")
	password = request.POST.get("password", "")
	if auth_agente(request, email, password) or logged_in(request) == "agente":
		agente = Agente.objects.get(id=request.session['id'])
		tickets_index = agente.ticket_set.all()
		return render_to_response("ticketmaster/tickets.html",
							   {"tickets" : tickets_index,
							   "agente" : agente})
	else:
		return render_to_response("ticketmaster/login.html")

def ventas(request,):
	email = request.POST.get("email", "")
	password = request.POST.get("password", "")
	if auth_supervisor(request, email, password) or logged_in(request) == "supervisor":
		tickets = Ticket.objects.all()
		return render_to_response("ticketmaster/ventas.html",
								   {"tickets" : tickets})
	else:
		return render_to_response("ticketmaster/login.html")

# @ensure_csrf_cookie
def new_ticket(request,):
	num = request.POST.get("num", "")
	agente_id = request.POST.get("id", "")
	for i in range(int(num)):
		t = Ticket(ticket_estado='abierto', agente_id=agente_id)
		t.save()
	agentes_index = Agente.objects.all()
	tickets = len(Agente.objects.get(id=1).ticket_set.all())
	return render_to_response("ticketmaster/agentes.html",
							   {"agentes" : agentes_index,
							   "tickets" : tickets})

def estado(request,):
	estado = request.POST.get("estado", "")
	ticket_id = request.POST.get("id", "")
	t = Ticket.objects.get(id=ticket_id)
	if estado == "cerrado":
		t.delete()
	else:
		t.ticket_estado = estado
		t.save()
	agente = Agente.objects.get(id=request.session['id'])
	tickets_index = agente.ticket_set.all()
	return render_to_response("ticketmaster/tickets.html",
							   {"tickets" : tickets_index,
							   "agente" : agente})

def logout(request,):
	request.session.clear()
	return render_to_response("ticketmaster/home.html")



