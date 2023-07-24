from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='proyecto'),
    path('view/<int:id>', views.view, name='proyecto_view'),
    path('edit/<int:id>', views.edit, name='proyecto_edit'),
    path('create/', views.create, name='proyecto_create'),
    path('delete/<int:id>', views.delete, name='proyecto_delete'),

]