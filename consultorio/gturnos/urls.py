from django.conf.urls import include, url
from . import views,turnoViews,buscadorViews,selectoresViews,medicoViews,pacienteViews
from django.views.generic import TemplateView

urlpatterns = [
        url(r'^$', views.index),
        url(r'^organizacion/new/$', views.organizacion_new, name='organizacion_new'),
        url(r'^organizacion/(?P<pk>[0-9]+)/edit/$', views.organizacion_edit, name='organizacion_edit'),
        url(r'^organizacion/(?P<pk>[0-9]+)/$', views.organizacion_detail),
        url(r'^organizacion/all/$', views.organizacion_all, name='organizacion_all'),

        #Turnos
        url(r'^turno/new/$', turnoViews.turno_new, name='turno_new'),

        #Turnos
        url(r'^turno/calendario/$', turnoViews.turnos_calendario, name='calendario'),
        url(r'^turno/(?P<pk>[0-9]+)/$', turnoViews.turno_detail,name='turno_detail'),

        #Paciente
        
        url(r'^paciente/(?P<pk>[0-9]+)/edit/$', pacienteViews.paciente_edit, name='paciente_edit'),
        url(r'^paciente/(?P<pk>[0-9]+)/delete/$', pacienteViews.paciente_delete, name='paciente_delete'),
        url(r'^paciente/all/$', pacienteViews.paciente_all, name='paciente_all'),
        url(r'^paciente/nuevo/$', pacienteViews.paciente_nuevo, name='paciente_nuevo'),
        url(r'^paciente/detail/(?P<pk>[0-9]+)/$', pacienteViews.paciente_detail, name='paciente_detail'),

        #Medico
        
        url(r'^medico/(?P<pk>[0-9]+)/edit/$', medicoViews.medico_edit, name='medico_edit'),
        url(r'^medico/(?P<pk>[0-9]+)/delete/$', medicoViews.medico_delete, name='medico_delete'),
        url(r'^medico/detail/(?P<pk>[0-9]+)/$', medicoViews.medico_detail, name='medico_detail'),
        url(r'^medico/all/$', medicoViews.medico_all, name='medico_all'),
        url(r'^medico/nuevo/$', medicoViews.medico_nuevo, name='medico_nuevo'),

        url(r'^historia/new/$', views.historia_new, name='historia_new'),
        url(r'^historia/(?P<pk>[0-9]+)/edit/$', views.historia_edit, name='historia_edit'),
        url(r'^historia/(?P<pk>[0-9]+)/$', views.historia_detail),
        url(r'^historia/all/$', views.historia_all, name='historia_all'),

        #Selector
        url(r'^selectores/buscar/$', buscadorViews.pacientesPorDni, name='buscar_paciente'),


        #Probando PopUp
        #url(r'^selectores/popup/$', buscadorViews.popup, name='popup'),

        #url(r'^foo/$', buscadorViews.prueba, name='prueba'),

        #url(r'^foo/$', TemplateView.as_view(template_name='gturnos/selectores/primera.html')),
        #url(r'^foo2/$', TemplateView.as_view(template_name='gturnos/selectores/segunda.html')),

        url(r'^buscarPaciente/$', selectoresViews.selectorPacientes, name='selector_paciente'),
        url(r'^buscarMedico/$', selectoresViews.selectorMedicos, name='selector_medico'),
        url(r'^buscarOrg/$', selectoresViews.selectorOrg, name='selector_org'),

        
        #url(r'^turno/nuevo/$', selectoresViews.selectorPaciente ,name='nuevoTurno'),
        url(r'^turno/nuevo/$', TemplateView.as_view(template_name='gturnos/turno/nuevoTurno.html'), name='nuevo_turno'),

        url(r'^agregarTurno/$', turnoViews.turno_nuevo, name='agregarTurno'),
        #url(r'^medico/nuevoMedico/$', nuevoMedico(template_name='gturnos/medico/nuevoMedico.html')),


    ]