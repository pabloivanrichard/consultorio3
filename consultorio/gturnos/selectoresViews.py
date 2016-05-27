from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from django.views.generic.base import TemplateView
from .forms import *



#------------------------------------------------------------------------------
#esta funcion filtra los pacientes ya sea por documento, nombre y apellido
#se pueden convinar
def selectorPacientes(request):
	#pregunto si el metodo de envio de datos es POST(si se envian datos, si no devuelvo un formulario de busqueda vacio)
	if request.method == "POST":	
	#obtengo los valos de los inputTExt del formulario	
	    q = request.POST['dni']
	    q1 = request.POST['nombre']
	    q2 = request.POST['apellido']
	    #creo una lista vacia en caso de no encontrar ningun objeto
	    pacientes = []

	    #convino los filtros de busqueda teniendo en cuenta los campos que lleno el usuario en el fomrulario
	    if q:
	    	pacientes = Paciente.objects.filter(dni=q) 	#| \
	    	#		Paciente.objects.filter(nombres__icontains=q1) | \
	    	#		Paciente.objects.filter(apellido__icontains=q2)
	    if q1:
	    	pacientes = Paciente.objects.filter(nombres__icontains=q1)
	    			
	    if q2:
	    	pacientes = Paciente.objects.filter(apellido__icontains=q2)	    
	    if q and q1:
	    	pacientes = Paciente.objects.filter(dni=q)# 	| \
	    	pacientes = pacientes.filter(nombres__icontains=q1) #| \
	    			#Paciente.objects.filter(apellido__icontains=q2)			
	    if q and q2:
	    	#pacientes = Paciente.objects.filter(dni=q) | \
	    	#			Paciente.objects.filter(apellido__icontains=q2)
	    	pacientes = Paciente.objects.filter(dni=q)
	    	pacientes = pacientes.filter(apellido__icontains=q2)
	    if q1 and q2:
	    	pacientes = Paciente.objects.filter(nombres__icontains=q1)# | \
	    	pacientes = pacientes.filter(apellido__icontains=q2)
	    				#Paciente.objects.filter(apellido__icontains=q2)
	    if q and q1 and q2:
	    	pacientes = Paciente.objects.filter(dni=q)# 	| \
	    	pacientes = pacientes.filter(nombres__icontains=q1)# | \
	    	pacientes = pacientes.filter(apellido__icontains=q2)
	    

	    #creo un nuevo formulario
	    form = buscadorPacienteForm()
	    #pregunto si hubo resultado en la busqueda, si no devulvo el formulario para realizar otra consulta
	    if len(pacientes) != 0:
	    	
	    	return render(request, 'gturnos/selectores/selectorPacientes.html', {'pacientes':pacientes, 'form':form})			
	    else:
	    	return render(request, 'gturnos/selectores/selectorPacientes.html', {'form':form})

	else:		
		form = buscadorPacienteForm()
		return render(request, 'gturnos/selectores/selectorPacientes.html', {'form':form})

