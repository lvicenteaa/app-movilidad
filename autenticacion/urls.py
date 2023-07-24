from django.urls import path

from .views import VRegistro


urlpatterns = [
    path('', VRegistro.as_view(), name='autenticacion'),
    path('cerrar_sesion/', cerrar_sesion, name='cerra_sesion'),
    path('logear/', logear, name='logear'),
]