from __future__ import unicode_literals

from django.db import models

class Supervisor(models.Model):
	supervisor_email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
	supervisor_password = models.CharField(max_length=200)

class Agente(models.Model):
	agente_email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
	agente_password = models.CharField(max_length=200)

class Ticket(models.Model):
	OPCIONES= (('a', 'Abierto'), ('p', 'Pendiente'), ('c', 'Cerrado'))
	ticket_estado = models.CharField(max_length=200, choices=OPCIONES, default='a')