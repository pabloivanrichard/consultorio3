

from django.db import models
from django.utils import timezone
from datetime import datetime   

class Sexo(models.Model):
	descripcion = models.CharField(max_length=15)
	def __str__(self):
		return self.descripcion

class Persona(models.Model):
	apellido = models.CharField(max_length=50)
	nombres = models.CharField(max_length=100)
	fecha_nac = models.DateField()
	domicilio = models.CharField(max_length=200)
	telefono = models.CharField(max_length=15)
	dni = models.IntegerField()
	sexo = models.ForeignKey(Sexo)
	def __str__(self):
		return self.nombres +' '+self.apellido

class Especialidad(models.Model):
	nombre = models.CharField(max_length=100)
	# mat_especialidad = models.IntegerField()
	def __str__(self):
		return self.nombre

class Organizacion(models.Model):
	nombre = models.CharField(max_length=100)
	domicilio = models.CharField(max_length=200)
	telefono = models.CharField(max_length=15)
	def __str__(self):
		return self.nombre
		
class Medico(Persona):
	mat_profesional = models.IntegerField()	
	organizaciones = models.ManyToManyField(Organizacion)

class Rel_Med_Esp(models.Model):
	mat_especialidad = models.IntegerField()
	medico = models.ForeignKey(Medico)
	especialidad = models.ForeignKey(Especialidad)

class Paciente(Persona):
	#persona = models.ForeignKey(Personas)
	fecha_inicio = models.DateField()
	altura = models.IntegerField()
	peso = models.IntegerField()
	perimetro_enc = models.IntegerField()
	
class Historia_medica(models.Model):
	paciente = models.ForeignKey(Paciente)
	medico = models.ForeignKey(Medico)
	fecha_historia = models.DateTimeField()
	diagnostico = models.CharField(max_length=500)
	tratamiento = models.CharField(max_length=500)

class Organizacion(models.Model):
	nombre = models.CharField(max_length=100)
	domicilio = models.CharField(max_length=200)
	telefono = models.CharField(max_length=15)
	def __str__(self):
		return self.nombre

class Turno(models.Model):
	medico = models.ForeignKey(Medico)
	paciente = models.ForeignKey(Paciente)
	# usuario = models.ForeignKey(Usuario)
	fecha_inicio = models.DateTimeField()
	fecha_fin = models.DateTimeField()
	#organizacion = models.ForeignKey(Organizacion)
