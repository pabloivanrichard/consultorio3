from django.conf.urls import include, url
from . import views,turnoViews

urlpatterns = [
        url(r'^$', views.index),
        url(r'^organizacion/new/$', views.organizacion_new, name='organizacion_new'),
        url(r'^organizacion/(?P<pk>[0-9]+)/edit/$', views.organizacion_edit, name='organizacion_edit'),
        url(r'^organizacion/(?P<pk>[0-9]+)/$', views.organizacion_detail),
        url(r'^organizacion/all/$', views.organizacion_all, name='organizacion_all'),
        #Persona
        # url(r'^persona/new/$', views.persona_new, name='persona_new'),
        # url(r'^persona/(?P<pk>[0-9]+)/edit/$', views.persona_edit, name='persona_edit'),
        # url(r'^persona/(?P<pk>[0-9]+)/$', views.persona_detail),
        # url(r'^persona/all/$', views.persona_all, name='persona_all'),

        #Turnos
        url(r'^turno/new/$', views.turno_new, name='turno_new'),

        #Turnos
        url(r'^turno/calendario/$', turnoViews.turnos_calendario, name='calendario'),

        #Paciente
        url(r'^paciente/new/$', views.paciente_new, name='paciente_new'),
        url(r'^paciente/(?P<pk>[0-9]+)/edit/$', views.paciente_edit, name='paciente_edit'),
        url(r'^paciente/(?P<pk>[0-9]+)/$', views.paciente_detail),
        url(r'^paciente/all/$', views.paciente_all, name='paciente_all'),

        url(r'^medico/new/$', views.medico_new, name='medico_new'),
        url(r'^medico/(?P<pk>[0-9]+)/edit/$', views.medico_edit, name='medico_edit'),
        url(r'^medico/(?P<pk>[0-9]+)/$', views.medico_detail),
        url(r'^medico/all/$', views.medico_all, name='medico_all'),

        url(r'^historia/new/$', views.historia_new, name='historia_new'),
        url(r'^historia/(?P<pk>[0-9]+)/edit/$', views.historia_edit, name='historia_edit'),
        url(r'^historia/(?P<pk>[0-9]+)/$', views.historia_detail),
        url(r'^historia/all/$', views.historia_all, name='historia_all'),
    ]