from django.conf.urls import url
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'api'
urlpatterns = [
    url(r'^empleado/$', views.CrearEmpleadoView.as_view(), name="create"),
    url(r'^empleado/(?P<pk>[0-9]+)/$', views.ListaEmpleadoView.as_view(), name="details"),
    url(r'^signosVitales/$', views.CrearSignosVitalesView.as_view(), name="create"),
    url(r'^signosVitales/(?P<pk>[0-9]+)/$', views.ListaSignosVitalesView.as_view(), name="details"),
    url(r'^consultaMedica/$', views.CrearConsultaMedicaView.as_view(), name="create"),
    url(r'^consultaMedica/(?P<pk>[0-9]+)/$', views.ListaConsultaMedicaView.as_view(), name="details"),
    url(r'^atencionEnfermeria/$', views.CrearAtencionEnfermeriaView.as_view(), name="create"),
    url(r'^atencionEnfermeria/(?P<pk>[0-9]+)/$', views.ListaAtencionEnfermeriaView.as_view(), name="details"),
    url(r'^permisoMedico/$', views.CrearPermisoMedicoView.as_view(), name="create"),
    url(r'^permisoMedico/(?P<pk>[0-9]+)/$', views.ListaPermisoMedicoView.as_view(), name="details"),
    url(r'^enfermedad/$', views.CrearEnfermedadView.as_view(), name="create"),
    url(r'^enfermedad/(?P<pk>[0-9]+)/$', views.ListaEnfermedadView.as_view(), name="details"),
    url(r'^diagnostico/$', views.CrearDiagnosticoView.as_view(), name="create"),
    url(r'^diagnostico/(?P<pk>[0-9]+)/$', views.ListaDiagnosticoView.as_view(), name="details"),
    url(r'^chequeo/$', views.CrearChequeoView.as_view(), name="create"),
    url(r'^chequeo/(?P<pk>[0-9]+)/$', views.ListaChequeoView.as_view(), name="details"),
    url(r'^fichaMedica/$', views.CrearFichaMedicaView.as_view(), name="create"),
    url(r'^fichaMedica/(?P<pk>[0-9]+)/$', views.ListaFichaMedicaView.as_view(), name="details"),
    url(r'^antecedentePatologicoPersonal/$', views.CrearAntecedentePatologicoPersonal.as_view(), name="create"),
    url(r'^antecedentePatologicoPersonal/(?P<pk>[0-9]+)/$', views.ListaAntecedentePatologicoPersonalView.as_view(), name="details"),
    url(r'^revisionAparatoSistema/$', views.CrearRevisionAparatoSistemaView.as_view(), name="create"),
    url(r'^revisionAparatoSistema/(?P<pk>[0-9]+)/$', views.ListaRevisionAparatoSistemaView.as_view(), name="details"),
    url(r'^aparatoSistema/$', views.CrearAparatoSistemaView.as_view(), name="create"),
    url(r'^aparatoSistema/(?P<pk>[0-9]+)/$', views.ListaAparatoSistemaView.as_view(), name="details"),
    url(r'^antecedenteLaboral/$', views.CrearAntecedenteLaboralView.as_view(), name="create"),
    url(r'^antecedenteLaboral/(?P<pk>[0-9]+)/$', views.ListaAntecedenteLaboralView.as_view(), name="details"),
    url(r'^empresa/$', views.CrearEmpresaView.as_view(), name="create"),
    url(r'^empresa/(?P<pk>[0-9]+)/$', views.ListaEmpresaView.as_view(), name="details"),
    url(r'^antecedentePatologicoFamiliar/$', views.CrearAntecedentePatologicoFamiliarView.as_view(), name="create"),
    url(r'^antecedentePatologicoFamiliar/(?P<pk>[0-9]+)/$', views.ListaAntecedentePatologicoFamiliarView.as_view(), name="details"),
    url(r'^Inmunizacion/$', views.CrearInmunizacionView.as_view(), name="create"),
    url(r'^Inmunizacion/(?P<pk>[0-9]+)/$', views.ListaInmunizacionView.as_view(), name="details"),
    url(r'^vacuna/$', views.CrearVacunaView.as_view(), name="create"),
    url(r'^vacuna/(?P<pk>[0-9]+)/$', views.ListaVacunaView.as_view(), name="details"),
    url(r'^examenLaboratorio/$', views.CrearExamenLaboratorioView.as_view(), name="create"),
    url(r'^examenLaboratorio/(?P<pk>[0-9]+)/$', views.ListaExamenLaboratorioView.as_view(), name="details"),
    url(r'^somaticoGeneral/$', views.CrearSomaticoGeneralView.as_view(), name="create"),
    url(r'^somaticoGeneral/(?P<pk>[0-9]+)/$', views.ListaSomaticoGeneralView.as_view(), name="details"),
    url(r'^regional/$', views.CrearRegionalView.as_view(), name="create"),
    url(r'^regional/(?P<pk>[0-9]+)/$', views.ListaRegionalView.as_view(), name="details"),
    url(r'^columna/$', views.CrearColumnaView.as_view(), name="create"),
    url(r'^columna/(?P<pk>[0-9]+)/$', views.ListaColumnaView.as_view(), name="details"),
    url(r'^regionLumbar/$', views.CrearRegionLumbarView.as_view(), name="create"),
    url(r'^regionLumbar/(?P<pk>[0-9]+)/$', views.ListaRegionLumbarView.as_view(), name="details"),
    url(r'^extremidades/$', views.CrearExtremidadesView.as_view(), name="create"),
    url(r'^extremidades/(?P<pk>[0-9]+)/$', views.ListaExtremidadesView.as_view(), name="details"),
    url(r'^examenFisico/$', views.CrearExamenFisicoView.as_view(), name="create"),
    url(r'^examenFisico/(?P<pk>[0-9]+)/$', views.ListaExamenFisicoView.as_view(), name="details"),
    url(r'^usuario/', views.ingresoUsuario, name="hello"),
]

urlpatterns = format_suffix_patterns(urlpatterns)