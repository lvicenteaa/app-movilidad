from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('perfil/', views.home, name='home'),
    path('eventos/', views.eventos, name='eventos'),
    path('movilidades/', views.movilidades, name='movilidades'),
    path('modalidades/', views.modalidades, name='modalidades'),
    path('tipos/', views.tipos, name='tipos'),
    path('', views.index, name='index'),

]