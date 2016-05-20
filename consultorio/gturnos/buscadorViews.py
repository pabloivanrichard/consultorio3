from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from django.views.generic.base import TemplateView
from .forms import *

#AGENTES
# def pacientesPorDni(request):
# 	if request.method == "GET":
# 		try:
# 	    	q = request.GET['dni']
# 	        posts = Paciente.objects.filter(documento__search=q) #| \
# 	                 #BlogPost.objects.filter(intro__search=q) | \
# 	                 #BlogPost.objects.filter(content__search=q)
# 	        return render_to_response(request, 'gturnos/selectores/buscadorPacientes.html', {'pacientes':pacientes})
# 	    except KeyError:
# 		#pacientes = Paciente.objects.all()
# 			return render(request, 'gturnos/selectores/buscadorPacientes.html', {'form':form})
# 			#return render(request, 'gturnos/selectores/buscadorPacientes.html', {'pacientes':pacientes})
# 	else:		
# 		form = buscadorForm()
# 		return render(request, 'gturnos/selectores/buscadorPacientes.html', {'form':form})


#------------------------------------------------------------------------------
#esta funcion filtra los pacientes ya sea por documento, nombre y apellido
#se pueden combinar
def pacientesPorDni(request):
	#pregunto si el metodo de envio de datos es POST(si se envian datos, si no devuelvo un formulario de busqueda vacio)
	if request.method == "POST":	
	#obtengo los valos de los inputTExt del formulario	
	    q = request.POST['dni']
	    q1 = request.POST['nombre']
	    q2 = request.POST['apellido']
	    #creo una lista vacia en caso de no encontrar ningun objeto
	    pacientes = []

	    #combino los filtros de busqueda teniendo en cuenta los campos que lleno el usuario en el fomrulario
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
	    form = buscadorForm()
	    #pregunto si hubo resultado en la busqueda, si no devuelvo el formulario para realizar otra consulta
	    if len(pacientes) != 0:
	    	
	    	return render(request, 'gturnos/selectores/buscadorPacientes.html', {'pacientes':pacientes, 'form':form})			
	    else:
	    	return render(request, 'gturnos/selectores/buscadorPacientes.html', {'form':form})

	else:		
		form = buscadorForm()
		return render(request, 'gturnos/selectores/buscadorPacientes.html', {'form':form})

		#http://pythoncentral.io/how-to-use-python-django-forms/
#------------------------------------------------------------------------------

# def search(request):
#     try:
#         q = request.GET['q']
#         posts = BlogPost.objects.filter(title__search=q) | \
#                 BlogPost.objects.filter(intro__search=q) | \
#                 BlogPost.objects.filter(content__search=q)
#         return render_to_response('search/results.html', {'posts':posts, 'q':q})
#     except KeyError:
#         return render_to_response('search/results.html')


# def busqueda(request):
#          if request.is_ajax():
#                    proyectos = Proyecto.objects.filter(nombre__startswith= request.GET['nombre'] ).values('nombre', 'id')
#                    return HttpResponse( json.dumps( list(proyectos)), content_type='application/json' ) 
#           else:
#                    return HttpResponse("Solo Ajax");

#  https://codigofacilito.com/articulos/como-crear-un-buscador-con-django

def popup(request):
	#turnoTodos = Turno.objects.all()
	form = buscadorForm()
	return render(request, 'gturnos/selectores/popup.html', {'form':form})