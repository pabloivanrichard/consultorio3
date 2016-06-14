#turnos views
from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from django.views.generic.base import TemplateView
from .forms import *
from datetime import *
from django.utils import timezone
import datetime


def turnos_calendario(request):
	turnosTodos = Turno.objects.all()	
	return render(request, 'gturnos/turno/calendario.html', {'turnos':turnosTodos})

def turno_new(request):
	if request.method == "POST":
		form = TurnoForm(request.POST)
		if form.is_valid():
			turno = form.save()
			return redirect('gturnos.turnoViews.turno_detail',pk=turno.pk)
	else:		
		form = TurnoForm()
		return render(request, 'gturnos/turno/new.html', {'form':form})

def turno_detail(request, pk):
	turno = get_object_or_404(Turno, pk=pk)	
	return render(request, 'gturnos/turno/detail.html', {'turno':turno})

def turno_all(request):
	turnoTodos = Turno.objects.all()
	return render(request, 'gturnos/turno/turnoList.html', {'turnoTodos':turnoTodos})


def turno_nuevo(request):
	if request.method == "POST":
		errores = []
		hayErrores = False
		#form = TurnoForm()
		#form.fecha_inicio = request.POST['fechaInicio']
		#form['fecha_inicio'] = datetime.now()
		#form.fecha_fin = datetime.now()
		fechaInicio = request.POST['fechaInicio']
		fecha1 = datetime.date(request.POST['fechaInicio'])
		hora1 = datetime.time(request.POST['horaInicio'])
		#date_processing = fechaInicio.replace('T', '-').replace(':', '-').split('-')
		#date_processing = [int(v) for v in date_processing]
		#fecha = datetime.datetime(*date_processing)
		fechaInicio = datetime.datetime.combine(fecha1, hora1)
		#fecha = datetime.datetime(fechaInicio)
		#fecha = datetime.fromtimestamp(fechaInicio)
		#delta = datetime.timedelta(minutes=15)
		medico1 = request.POST['hmedico']
		if len(medico1) == 0:
			errores.append("Debe seleccionar un medico")
			hayErrores = True
			#return render(request, 'gturnos/turno/nuevoTurno.html', {'errores':errores})
		else:
			medico1 = Medico.objects.get(pk=request.POST['hmedico'])

		paciente1 = request.POST['hpaciente']
		if len(paciente1) == 0:
			errores.append("Debe seleccionar un Paciente")
			hayErrores = True
			#return render(request, 'gturnos/turno/nuevoTurno.html', {'errores':errores})
		else:
			paciente1 = Paciente.objects.get(pk=request.POST['hpaciente'])
		
		if 	hayErrores:
			return render(request, 'gturnos/turno/nuevoTurno.html', {'errores':errores,'fechaInicio':fechaInicio,'fecha':fecha})
		else: #datetime.now()
			nuevoTurno = Turno(fecha_inicio=fechaInicio,fecha_fin = fechaInicio, medico = medico1,paciente = paciente1)
			nuevoTurno.save()
			return redirect('turno_detail',pk=nuevoTurno.pk)
		
	else:		
		form = TurnoForm()
		return render(request, 'nuevo_turno', {})
