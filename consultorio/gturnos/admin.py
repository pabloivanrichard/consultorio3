from django.contrib import admin

# Register your models here.
# from .models import ObraSocial,Paciente,Turno

# admin.site.register(ObraSocial)
# admin.site.register(Paciente)
# admin.site.register(Turno)

from .models import *

admin.site.register(Persona)
# admin.site.register(Tipo_Usuario)
admin.site.register(Especialidad)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Historia_medica)
admin.site.register(Organizacion)
# admin.site.register(Usuario)
admin.site.register(Turno)
admin.site.register(Sexo)
admin.site.register(Rel_Med_Esp)