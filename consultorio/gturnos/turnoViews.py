#turnos views
from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from django.views.generic.base import TemplateView
from .forms import *


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