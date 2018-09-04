from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


# Create your views here.
def vista_inicio(request):
	return render(request,'inicio.html')







def vista_lista_mecanico(request):
	mecanico=Mecanico.objects.all()
	return render (request, 'lista_mecanico.html', locals())



def vista_ver_mecanico (request, id_meca):

	p= Mecanico.objects.get(id = id_meca)
	return render(request, 'ver_mecanico.html', locals())


def vista_agregar_mecanico (request):
	if request.method == 'POST':
		formulario = agregar_mecanico_form(request.POST,request.FILES)
		if formulario.is_valid():
			meca = formulario.save(commit= False)
			meca.status = True
			meca.save()
			formulario.save_m2m()
			return redirect ('/lista_mecanico/')
	else:
			formulario = agregar_mecanico_form()
	return render(request, 'agregar_mecanico.html', locals())


def vista_editar_mecanico (request, id_meca):
	meca =Mecanico.objects.get(id =id_meca)
	#Select * from home_auto where id== id_prod;
	formulario=agregar_mecanico_form(instance = meca )
	if request.method== "POST":
		formulario=agregar_mecanico_form(request.POST,request.FILES,instance= meca)
		formulario.save()
		meca.save()
		msj="se guardó correctamente"
	return render(request, 'agregar_mecanico.html', locals())


def vista_eliminar_mecanico (request, id_meca):
	meca =Mecanico.objects.get(id =id_meca)
	meca.delete()
	return redirect('/lista_mecanico/')





#---------------------------------------------------------------------------------------------------------------------------------------------





def vista_lista_auto (request):
	auto = Auto.objects.all()
	return render(request, 'lista_auto.html', locals())



def vista_agregar_auto (request):
	if request.method == 'POST':
		formulario = agregar_auto_form(request.POST,request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit= False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/lista_auto/')
	else:
			formulario = agregar_auto_form()
	return render(request, 'agregar_auto.html', locals())

def vista_ver_producto (request, id_prod):

	p = Auto.objects.get(id = id_prod)
	
	

	return render(request, 'ver_producto.html', locals())


def vista_editar_auto (request, id_prod):
	pro =Auto.objects.get(id =id_prod)
	#Select * from home_auto where id== id_prod;
	formulario=agregar_auto_form(instance = pro )
	if request.method== "POST":
		formulario=agregar_auto_form(request.POST,request.FILES,instance= pro)
		formulario.save()
		pro.save()
		msj="se guardó correctamente"
	return render(request, 'agregar_auto.html', locals())

	
def vista_eliminar_auto (request, id_prod):
	pro =Auto.objects.get(id =id_prod)
	pro.delete()
	return redirect('/lista_auto/')







#---------------------------------------------------------------------------------------------------------------------------------------------






def vista_lista_patrocinador (request):
	patro = Patrocinador.objects.all()
	return render(request, 'lista_patrocinador.html', locals())



def vista_agregar_patrocinador (request):
	if request.method == 'POST':
		formulario = agregar_patrocinador_form(request.POST,request.FILES)
		if formulario.is_valid():
			patro = formulario.save(commit= False)
			patro.status = True
			patro.save()
			formulario.save_m2m()
			return redirect ('/lista_patrocinador/')
	else:
			formulario = agregar_patrocinador_form()
	return render(request, 'agregar_patrocinador.html', locals())

def vista_ver_patrocinador (request, id_patro):

	p = Patrocinador.objects.get(id = id_patro)
	return render(request, 'ver_patrocinador.html', locals())


def vista_editar_patrocinador (request, id_patro):
	patro =Patrocinador.objects.get(id =id_patro)
	#Select * from home_auto where id== id_prod;
	formulario=agregar_patrocinador_form(instance = patro )
	if request.method== "POST":
		formulario=agregar_patrocinador_form(request.POST,request.FILES,instance= patro)
		formulario.save()
		patro.save()
		msj="se guardó correctamente"
	return render(request, 'agregar_patrocinador.html', locals())

	
def vista_eliminar_patrocinador (request, id_patro):
	patro =Patrocinador.objects.get(id =id_patro)
	patro.delete()
	return redirect('/lista_patrocinador/')




#---------------------------------------------------------------------------------------------------------------------------------------------






def vista_lista_piloto (request):
	pilo = Piloto.objects.all()
	return render(request, 'lista_piloto.html', locals())



def vista_agregar_piloto (request):
	if request.method == 'POST':
		formulario = agregar_piloto_form(request.POST,request.FILES)
		if formulario.is_valid():
			pilo = formulario.save(commit= False)
			pilo.status = True
			pilo.save()
			formulario.save_m2m()
			return redirect ('/lista_piloto/')
	else:
			formulario = agregar_piloto_form()
	return render(request, 'agregar_piloto.html', locals())

def vista_ver_piloto (request, id_pilo):


	p = Piloto.objects.get(id = id_pilo)
	return render(request, 'ver_piloto.html', locals())


def vista_editar_piloto (request, id_pilo):
	pilo =Piloto.objects.get(id =id_pilo)
	#Select * from home_auto where id== id_prod;
	formulario=agregar_piloto_form(instance = pilo )
	if request.method== "POST":
		formulario=agregar_piloto_form(request.POST,request.FILES,instance= pilo)
		formulario.save()
		pilo.save()
		msj="se guardó correctamente"
	return render(request, 'agregar_piloto.html', locals())

	
def vista_eliminar_piloto (request, id_pilo):
	pilo =Piloto.objects.get(id =id_pilo)
	pilo.delete()
	return redirect('/lista_piloto/')






#---------------------------------------------------------------------------------------------------------------------------------------------






def vista_lista_carrera (request):
	carre = Carrera.objects.all()
	return render(request, 'lista_carrera.html', locals())



def vista_agregar_carrera (request):
	if request.method == 'POST':
		formulario = agregar_carrera_form(request.POST,request.FILES)
		if formulario.is_valid():
			carre = formulario.save(commit= False)
			carre.status = True
			carre.save()
			formulario.save_m2m()
			return redirect ('/lista_carrera/')
	else:
			formulario = agregar_carrera_form()
	return render(request, 'agregar_carrera.html', locals())

def vista_ver_carrera (request, id_carre):

	p = Carrera.objects.get(id = id_carre)
	return render(request, 'ver_carrera.html', locals())


def vista_editar_carrera (request, id_carre):
	carre =Carrera.objects.get(id =id_carre)
	#Select * from home_auto where id== id_prod;
	formulario=agregar_carrera_form(instance = carre )
	if request.method== "POST":
		formulario=agregar_carrera_form(request.POST,request.FILES,instance= carre)
		formulario.save()
		carre.save()
		msj="se guardó correctamente"
	return render(request, 'agregar_carrera.html', locals())

	
def vista_eliminar_carrera (request, id_carre):
	carre =Carrera.objects.get(id =id_carre)
	carre.delete()
	return redirect('/lista_carrera/')




def vista_login (request):
	usu =''
	cla =''
	if request.method == 'POST':
		formulario= login_form (request.POST)
		if formulario.is_valid():
			usu=formulario.cleaned_data['usuario']
			cla=formulario.cleaned_data['clave']
			usuario= authenticate(username=usu,password=cla)
			if usuario is not None and usuario.is_active:
				login(request,usuario)
				return redirect('/')
			else:
				msj="usuario o claves no coinciden"
	formulario=login_form()
	return render(request,'login.html',locals())

def vista_logout(request):
	logout(request)
	return redirect('/login/')


def vista_register (request):
	formulario=register_form()
	if request.method == 'POST':
		formulario=register_form(request.POST)
		if formulario.is_valid():
			usuario=formulario.cleaned_data['username']
			correo=formulario.cleaned_data['email']
			password_1=formulario.cleaned_data['password_1']
			password_2=formulario.cleaned_data['password_2']
			u=User.objects.create_user(username=usuario,email=correo,password=password_1)
			u.save
			return render(request,'tanks_for_register.html',locals())
		else:
			return render(request,'register.html',locals())
	return render(request,'register.html',locals())



def vista_tanks_for_register(request):
	return render(request,'tanks_for_register.html')


def vista_crear_perfil(request):
	form_1= register_form()
	form_2= perfil_form()
	if request.method=='POST':
		form_1= register_form(request.POST)
		form_2= perfil_form(request.POST, request.FILES)
		if form_1.is_valid() and form_2.is_valid():
			usuario=form_1.cleaned_data['username']
			correo=form_1.cleaned_data['email']
			password_1=form_1.cleaned_data['password_1']
			password_2=form_1.cleaned_data['password_2']
			u=User.objects.create_user(username=usuario,email=correo,password=password_1)
			u.save()

			y=form_2.save(commit=False)
			y.user=u
			y.save()
			return redirect ('/login/')
	return render(request,'crear_perfil.html',locals())



def vista_lista_perfil (request):
	perfil = Perfil.objects.all()
	return render(request, 'lista_perfil.html', locals())

	








