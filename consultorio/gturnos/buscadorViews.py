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

def pacientesPorDni(request):
	if request.method == "POST":		
	    q = request.GET['dni']
	    posts = Paciente.objects.filter(documento__search=q) #| \
	                 #BlogPost.objects.filter(intro__search=q) | \
	                 #BlogPost.objects.filter(content__search=q)
	    return render_to_response(request, 'gturnos/selectores/buscadorPacientes.html', {'pacientes':pacientes})			
	else:		
		form = buscadorForm()
		return render(request, 'gturnos/selectores/buscadorPacientes.html', {'form':form})

		#http://pythoncentral.io/how-to-use-python-django-forms/


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