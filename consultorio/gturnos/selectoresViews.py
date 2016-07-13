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

def selectorMedicos(request):
	#pregunto si el metodo de envio de datos es POST(si se envian datos, si no devuelvo un formulario de busqueda vacio)
	if request.method == "POST":	
	#obtengo los valos de los inputTExt del formulario	
	    q = request.POST['mat_profesional']
	    q1 = request.POST['nombre']
	    q2 = request.POST['apellido']
	    #creo una lista vacia en caso de no encontrar ningun objeto
	    medicos = []

	    #combino los filtros de busqueda teniendo en cuenta los campos que lleno el usuario en el fomrulario
	    if q:
	    	medicos = Medico.objects.filter(mat_profesional=q) 	#| \
	    	#		Paciente.objects.filter(nombres__icontains=q1) | \
	    	#		Paciente.objects.filter(apellido__icontains=q2)
	    if q1:
	    	medicos = Medico.objects.filter(nombres__icontains=q1)
	    			
	    if q2:
	    	medicos = Medico.objects.filter(apellido__icontains=q2)	    
	    if q and q1:
	    	medicos = Medico.objects.filter(mat_profesional=q)# 	| \
	    	medicos = medicos.filter(nombres__icontains=q1) #| \
	    			#Paciente.objects.filter(apellido__icontains=q2)			
	    if q and q2:
	    	#pacientes = Paciente.objects.filter(dni=q) | \
	    	#			Paciente.objects.filter(apellido__icontains=q2)
	    	medicos = Medico.objects.filter(mat_profesional=q)
	    	medicos = medicos.filter(apellido__icontains=q2)
	    if q1 and q2:
	    	medicos = Medico.objects.filter(nombres__icontains=q1)# | \
	    	medicos = medicos.filter(apellido__icontains=q2)
	    				#Paciente.objects.filter(apellido__icontains=q2)
	    if q and q1 and q2:
	    	medicos = Medico.objects.filter(mat_profesional=q)# 	| \
	    	medicos = medicos.filter(nombres__icontains=q1)# | \
	    	medicos = medicos.filter(apellido__icontains=q2)
	    

	    #creo un nuevo formulario
	    form = buscadorMedicoForm()
	    #pregunto si hubo resultado en la busqueda, si no devuelvo el formulario para realizar otra consulta
	    if len(medicos) != 0:
	    	
	    	return render(request, 'gturnos/selectores/selectorMedicos.html', {'medicos':medicos, 'form':form})			
	    else:
	    	return render(request, 'gturnos/selectores/selectorMedicos.html', {'form':form})

	else:		
		form = buscadorMedicoForm()
		return render(request, 'gturnos/selectores/selectorMedicos.html', {'form':form})


def selectorOrg(request):
	#pregunto si el metodo de envio de datos es POST(si se envian datos, si no devuelvo un formulario de busqueda vacio)
	if request.method == "POST":	
	#obtengo los valos de los inputTExt del formulario	
	    q = request.POST['nombre']
	    q1 = request.POST['domicilio']
	    q2 = request.POST['telefono']
	    #creo una lista vacia en caso de no encontrar ningun objeto
	    medicos = []

	    #combino los filtros de busqueda teniendo en cuenta los campos que lleno el usuario en el fomrulario
	    if q:
	    	organizaciones = Organizacion.objects.filter(nombre__icontains=q) 	#| \
	    	#		Paciente.objects.filter(nombres__icontains=q1) | \
	    	#		Paciente.objects.filter(apellido__icontains=q2)
	    if q1:
	    	organizaciones = Organizacion.objects.filter(domicilio__icontains=q1)
	    			
	    if q2:
	    	organizaciones = Organizacion.objects.filter(telefono__icontains=q2)	    
	    if q and q1:
	    	organizaciones = Organizacion.objects.filter(nombre__icontains=q)# 	| \
	    	organizaciones = organizaciones.filter(domicilio__icontains=q1) #| \
	    			#Paciente.objects.filter(apellido__icontains=q2)			
	    if q and q2:
	    	#pacientes = Paciente.objects.filter(dni=q) | \
	    	#			Paciente.objects.filter(apellido__icontains=q2)
	    	organizaciones = Organizacion.objects.filter(nombre__icontains=q)
	    	organizaciones = organizaciones.filter(telefono__icontains=q2)
	    if q1 and q2:
	    	organizaciones = Organizacion.objects.filter(domicilio__icontains=q1)# | \
	    	organizaciones = organizaciones.filter(telefono__icontains=q2)
	    				#Paciente.objects.filter(apellido__icontains=q2)
	    if q and q1 and q2:
	    	organizaciones = Organizacion.objects.filter(nombre__icontains=q)# 	| \
	    	organizaciones = organizaciones.filter(domicilio__icontains=q1)# | \
	    	organizaciones = organizaciones.filter(telefono__icontains=q2)
	    

	    #creo un nuevo formulario
	    form = buscadorOrgForm()
	    #pregunto si hubo resultado en la busqueda, si no devuelvo el formulario para realizar otra consulta
	    if len(organizaciones) != 0:
	    	
	    	return render(request, 'gturnos/selectores/selectorOrg.html', {'organizaciones':organizaciones, 'form':form})			
	    else:
	    	return render(request, 'gturnos/selectores/selectorOrg.html', {'form':form})

	else:		
		form = buscadorOrgForm()
		return render(request, 'gturnos/selectores/selectorOrg.html', {'form':form})