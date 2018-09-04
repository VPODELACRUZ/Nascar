from django.urls import path
from .views import *


urlpatterns = [
	path('lista_perfil/',vista_lista_perfil),
	path('crear_perfil/',vista_crear_perfil, name='vista_crear_perfil'), 
	path('tanks_for_register/',vista_tanks_for_register),
	path('login/',vista_login, name='vista_login'),
	path('logout/',vista_logout , name="vista_logout"),
	path('',vista_inicio),
	path('register/',vista_register, name='vista_register'),
	#-------------------------------------------------------------------
	path('lista_auto/',vista_lista_auto),
	path('agregar_auto/',vista_agregar_auto),
	path('ver_producto/<int:id_prod>/',vista_ver_producto, name='ver_producto'),
	path('eliminar_auto/<int:id_prod>/',vista_eliminar_auto, name='eliminar_auto'),
	path('editar_auto/<int:id_prod>/',vista_editar_auto, name='editar_auto'),
	#--------------------------------------------------------------------
	path('lista_mecanico/',vista_lista_mecanico),
	path('agregar_mecanico/',vista_agregar_mecanico),
	path('ver_mecanico/<int:id_meca>/',vista_ver_mecanico, name='ver_mecanico'),
	path('editar_mecanico/<int:id_meca>/',vista_editar_mecanico, name='editar_mecanico'),
	path('eliminar_mecanico/<int:id_meca>/',vista_eliminar_mecanico, name='eliminar_mecanico'),
	#--------------------------------------------------------------------
	path('lista_patrocinador/',vista_lista_patrocinador),
	path('agregar_patrocinador/',vista_agregar_patrocinador),
	path('ver_patrocinador/<int:id_patro>/',vista_ver_patrocinador, name='ver_patrocinador'),
	path('eliminar_patrocinador/<int:id_patro>/',vista_eliminar_patrocinador, name='eliminar_patrocinador'),
	path('editar_patrocinador/<int:id_patro>/',vista_editar_patrocinador, name='editar_patrocinador'),
	#--------------------------------------------------------------------
	path('lista_piloto/',vista_lista_piloto),
	path('agregar_piloto/',vista_agregar_piloto),
	path('ver_piloto/<int:id_pilo>/',vista_ver_piloto, name='ver_piloto'),
	path('eliminar_piloto/<int:id_pilo>/',vista_eliminar_piloto, name='eliminar_piloto'),
	path('editar_piloto/<int:id_pilo>/',vista_editar_piloto, name='editar_piloto'),
	#--------------------------------------------------------------------
	path('lista_carrera/',vista_lista_carrera),
	path('agregar_carrera/',vista_agregar_carrera),
	path('ver_carrera/<int:id_carre>/',vista_ver_carrera, name='ver_carrera'),
	path('eliminar_carrera/<int:id_carre>/',vista_eliminar_carrera, name='eliminar_carrera'),
	path('editar_carrera/<int:id_carre>/',vista_editar_carrera, name='editar_carrera'),
	
]