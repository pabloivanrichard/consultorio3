from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from django.views.generic.base import TemplateView
from .forms import *

def paciente_detail(request, pk):
	pac = get_object_or_404(Paciente, pk=pk)	
	return render(request, 'gturnos/paciente/detail.html', {'pac':pac})

def paciente_all(request):
	pacienteTodos = Paciente.objects.all()
	return render(request, 'gturnos/paciente/pacList.html', {'pacTodas':pacienteTodos})

def paciente_delete(request,pk):
	p = get_object_or_404(Paciente, pk=pk)
	p.delete()
	pacienteTodos = Paciente.objects.all()
	return render(request, 'gturnos/paciente/pacList.html', {'pacTodas':pacienteTodos})

def paciente_edit(request,pk):
	p = get_object_or_404(Paciente, pk=pk)
	errores=[]
	hay_error=False
	if request.method == "POST":
		
		
		pnombre=request.POST['nombre']
		papellido=request.POST['apellido']
		pdni=request.POST['dni']
		pfechanac=request.POST['fecha_nac']
		pdom=request.POST['domicilio']
		ptel=request.POST['tel']
		psex=request.POST['sexo']
		ppeso=request.POST['peso']
		palt=request.POST['altura']
		ppc=request.POST['pc']
		pfechacar=request.POST['fecha_car']

		
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
		if len(ppeso)==0:
			errores.append("Debe Ingresar el Peso del Paciente")
			hay_error=True
		if len(palt)==0:
			errores.append("Debe Ingresar la Altura del Paciente")
			hay_error=True
		if len(ppc)==0:
			errores.append("Debe Ingresar el Perimetro Encefalico")
			hay_error=True
		
		if hay_error:
			return render(request, 'gturnos/paciente/nuevoPaciente.html',{'errores':errores,'apellido':papellido,
				'tel':ptel,'dni':pdni,'fecha':pfechanac,'dom':pdom,'peso':ppeso,'nombre':pnombre,'altura':palt,
				'pc':ppc,'fecha_car':pfechacar})
		else:
			p.nombres=pnombre
			p.apellido=papellido
			p.dni=pdni
			p.fecha_nac=pfechanac
			p.dom=pdom
			p.telefono=ptel
			p.peso=ppeso
			p.altura=palt
			p.perimetro_enc=ppc
			p.fecha_inicio=pfechacar
			p.sexo=psexo
			
			p.save()

	else:		
			return render(request,'gturnos/paciente/nuevoPaciente.html',{'errores':errores,'apellido':p.apellido,
				'tel':p.telefono,'dni':p.dni,'fecha':p.fecha_nac,'dom':p.domicilio,'peso':p.peso,'nombre':p.nombres,'altura':p.altura,
				'pc':p.perimetro_enc,'fecha_car':p.fecha_inicio})

def paciente_nuevo(request):
	if request.method == "POST":
		errores=[]
		hay_error=False
		

		pnombre=request.POST['nombre']
		papellido=request.POST['apellido']
		pdni=request.POST['dni']
		pfechanac=request.POST['fecha_nac']
		pdom=request.POST['domicilio']
		ptel=request.POST['tel']
		psex=request.POST['sexo']
		ppeso=request.POST['peso']
		palt=request.POST['altura']
		ppc=request.POST['pc']
		pfechacar=request.POST['fecha_car']

		
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
		if len(ppeso)==0:
			errores.append("Debe Ingresar el Peso del Paciente")
			hay_error=True
		if len(palt)==0:
			errores.append("Debe Ingresar la Altura del Paciente")
			hay_error=True
		if len(ppc)==0:
			errores.append("Debe Ingresar el Perimetro Encefalico")
			hay_error=True
		
		if hay_error:
			return render(request, 'gturnos/paciente/nuevoPaciente.html',{'errores':errores,'apellido':papellido,
				'tel':ptel,'dni':pdni,'fecha':pfechanac,'dom':pdom,'peso':ppeso,'nombre':pnombre,'altura':palt,
				'pc':ppc,'fecha_car':pfechacar})
		else:
			nuevoPaciente=Paciente(nombres=pnombre,apellido=papellido,dni=pdni,domicilio=pdom,
				fecha_nac=pfechanac,sexo=psexo,fecha_inicio=pfechacar,peso=ppeso,altura=palt,perimetro_enc=ppc)
			
			nuevoPaciente.save()
			
			return redirect('paciente_detail',pk=nuevoPaciente.pk)
	else:
		return render(request,'gturnos/paciente/nuevoPaciente.html', {})

