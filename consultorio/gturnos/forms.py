from django import forms
from .models import *
from django.forms import  TextInput

class OrganizacionForm(forms.ModelForm):
	"""docstring for OrganizacionForm"""
	class Meta:
		model = Organizacion
		fields = ('nombre','domicilio','telefono')
		widgets = {
		'nombre': TextInput(attrs={'class':'form-control'}),
		'domicilio': TextInput(attrs={'class':'form-control'}),
		'telefono': TextInput(attrs={'class':'form-control'}),
		}
		
class PacienteForm(forms.ModelForm):
	"""docstring for PacienteForm"""
	class Meta:
		model = Paciente
		fields = ['apellido','nombres','dni','fecha_nac','altura','peso','perimetro_enc','domicilio','telefono','sexo','fecha_inicio']
		widgets = {
		'apellido': TextInput(attrs={'class':'form-control'}),
		'nombres': TextInput(attrs={'class':'form-control'}),
		'domicilio': TextInput(attrs={'class':'form-control'}),
		'telefono': TextInput(attrs={'class':'form-control'}),
		'dni': TextInput(attrs={'class':'form-control'}),
		'altura': TextInput(attrs={'class':'form-control'}),
		'peso': TextInput(attrs={'class':'form-control'}),
		'perimetro_enc': TextInput(attrs={'class':'form-control'}),
		}
		
class MedicoForm(forms.ModelForm):
	"""docstring for OrganizacionForm"""
	class Meta:
		model = Medico
		fields = ['apellido','nombres','dni','fecha_nac','domicilio','telefono','sexo','mat_profesional','organizaciones']
		widgets = {
		'apellido': TextInput(attrs={'class':'form-control'}),
		'nombres': TextInput(attrs={'class':'form-control'}),
		'domicilio': TextInput(attrs={'class':'form-control'}),
		'telefono': TextInput(attrs={'class':'form-control'}),
		'dni': TextInput(attrs={'class':'form-control'}),
		'mat_profesional': TextInput(attrs={'class':'form-control'}),
		}

class HistoriaForm(forms.ModelForm):
	"""docstring for OrganizacionForm"""
	class Meta:
		model = Historia_medica
		diagnostico=forms.CharField(widget=forms.Textarea)
		fields = ['fecha_historia','diagnostico','tratamiento','paciente','medico']
		# widgets = {

class TurnoForm(forms.ModelForm):
	"""docstring for OrganizacionForm"""
	class Meta:
		model = Turno		
		fields = ('fecha_inicio','fecha_fin','medico','paciente')
		#medico = forms.ModelChoiceField(label=u'Categoría', queryset = Medico.objects.all(), widget=forms.TextInput(attrs={'class':'form-control'}))
		#paciente = forms.ModelChoiceField(label=u'Categoría', queryset = Paciente.objects.all())
		#fecha = models.DateTimeField(default=datetime.now, blank=True)
		#widgets = {
		#'fecha': DateWidget(attrs={'id':"fecha"}, bootstrap_version=3),
		#'medico': TextInput(attrs={'class':'form-control'}),
		#'paciente': TextInput(attrs={'class':'form-control'}),
		#'organizacion': TextInput(attrs={'class':'form-control'})	
		#'fecha': TextInput(attrs={'class':'input-group date'})
		
		#}
		#fecha = forms.DateField(widget=forms.SelectDateWidget())

class buscadorForm(forms.Form):
	"""docstring for OrganizacionForm"""
	#class Meta:
	dni = forms.IntegerField(label=u'Documento')
	nombre = forms.CharField(label=u'Nombre')
	apellido = forms.CharField(label=u'Apellido')
		#diagnostico=forms.CharField(widget=forms.Textarea)
		#fields = ['fecha_historia','diagnostico','tratamiento','paciente','medico']


class buscadorPacienteForm(forms.Form):
	"""docstring for OrganizacionForm"""
	#class Meta:
	dni = forms.IntegerField(label=u'Documento')
	nombre = forms.CharField(label=u'Nombre')
	apellido = forms.CharField(label=u'Apellido')	

class buscadorMedicoForm(forms.Form):
	"""docstring for OrganizacionForm"""
	#class Meta:
	mat_profesional = forms.IntegerField(label=u'Matricula')
	nombre = forms.CharField(label=u'Nombre')
	apellido = forms.CharField(label=u'Apellido')


class buscadorOrgForm(forms.Form):
	"""docstring for OrganizacionForm"""
	#class Meta:
	nombre = forms.CharField(label=u'Nombre')
	domicilio = forms.CharField(label=u'Domicilio')
	telefono = forms.IntegerField(label=u'Telefono')
# class nuevoTurnoForm(forms.Form):
# 	"""docstring for OrganizacionForm"""
# 	#class Meta:
# 	fechaInicio = forms.CharField(label=u'Fecha y Hora de Inicio')
# 	paciente = forms.CharField(label=u'Paciente')
# 	medico = forms.CharField(label=u'Medico')
# 	h_paciente = forms.CharField(widget=forms.HiddenInput())
# 	h_medico = forms.CharField(widget=forms.HiddenInput())