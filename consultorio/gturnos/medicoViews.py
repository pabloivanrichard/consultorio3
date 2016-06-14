from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from django.views.generic.base import TemplateView
from .forms import *

def medico_nuevo(request):
	if request.method == "POST":
		errores=[]
		hay_error=False
		orgaList=[]

		pnombre=request.POST['nombre']
		papellido=request.POST['apellido']
		pdni=request.POST['dni']
		pfechanac=request.POST['fecha_nac']
		pdom=request.POST['domicilio']
		ptel=request.POST['tel']
		psex=request.POST['sexo']
		pmat=request.POST['mat']
		porg=request.POST['horganizacion']

		if len(porg)==0:
			errores.append("Debe seleccionar una Organizacion")
			hay_error=True
		else:
			porganizacion=Organizacion.objects.get(pk=porg)
			orgaList.append(porganizacion)
		
		psexo=Sexo.objects.get(pk=psex)

		if len(pnombre)==0:
			errores.append("Debe Ingresar el Nombre")
			hay_error=True
		if len(papellido)==0:
			errores.append("Debe Ingresar el Apellido")
			hay_error=True
		if len(pdom)==0:
			errores.append("Debe Ingresar el Domicilio")
			hay_error=True
		if len(pdni)==0:
			errores.append("Debe Ingresar el DNI")
			hay_error=True
		if len(ptel)==0:
			errores.append("Debe Ingresar el Telefono de Contacto")
			hay_error=True
		if len(pmat)==0:
			errores.append("Debe Ingresar la matricula del Profesional")
			hay_error=True

		if hay_error:
			return render(request, 'gturnos/medico/nuevoMedico.html',{'errores':errores,'apellido':papellido,
				'tel':ptel,'dni':pdni,'fecha':pfechanac,'dom':pdom,'mat':pmat,'nombre':pnombre,'organizacion':porganizacion})
		else:
			nuevoMedico=Medico(nombres=pnombre,apellido=papellido,dni=pdni,domicilio=pdom,
				fecha_nac=pfechanac,sexo=psexo,mat_profesional=pmat)
			
			nuevoMedico.save()
			nuevoMedico.organizaciones.add(porganizacion)
			return redirect('medico_detail',pk=nuevoMedico.pk)
	else:
		return render(request,'gturnos/medico/nuevoMedico.html', {})