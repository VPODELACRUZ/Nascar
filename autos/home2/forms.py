from django import forms
from .models import *
from django.contrib.auth.models import User




class agregar_auto_form(forms.ModelForm) :
    
    class Meta:
        model = Auto
        fields = ['nombre','modelo','marca','color','precio','cilindraje','dimensiones','peso','matricula','mecanico','foto','detalle']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'from-control2'}),
            'modelo': forms.TextInput(attrs={'class':'from-control2'}),
            'marca': forms.TextInput(attrs={'class':'from-control2'}),
            'color': forms.TextInput(attrs={'class':'from-control2'}),
            'precio': forms.TextInput(attrs={'class':'from-control2'}),
            'cilindraje': forms.TextInput(attrs={'class':'from-control2'}),
            'peso': forms.TextInput(attrs={'class':'from-control2'}),
            'matricula': forms.TextInput(attrs={'class':'from-control2'}),
            'dimensiones': forms.TextInput(attrs={'class':'from-control2'}),
            'mecanico': forms.SelectMultiple(attrs={'class':'from-control3'}),
            'foto': forms.ClearableFileInput(attrs={'class':'from-co'}),
            'detalle': forms.TextInput(attrs={'class':'from-control2'}),
            }


class agregar_mecanico_form(forms.ModelForm):
    class Meta:
        model = Mecanico 
        fields = ['nombre','apellido','edad','genero','cedula','direccion','lugar_nacimiento','web','foto','detalle']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'from-control2'}),
            'apellido': forms.TextInput(attrs={'class':'from-control2'}),
            'edad': forms.TextInput(attrs={'class':'from-control2'}),
            'genero': forms.TextInput(attrs={'class':'from-control2'}),
            'cedula': forms.TextInput(attrs={'class':'from-control2'}),
            'direccion': forms.TextInput(attrs={'class':'from-control2'}),
            'lugar_nacimiento': forms.TextInput(attrs={'class':'from-control2'}),
            'web': forms.TextInput(attrs={'class':'from-control2'}),
            'foto': forms.ClearableFileInput(attrs={'class':'from-co'}),
            'detalle': forms.TextInput(attrs={'class':'from-control2'}),
            }

class agregar_patrocinador_form(forms.ModelForm):
    class Meta:
        model = Patrocinador
        fields =[ 'nombre','telefono','direccion','web','foto','detalle']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'from-control2'}),
            'telefono': forms.TextInput(attrs={'class':'from-control2'}),
            'direccion': forms.TextInput(attrs={'class':'from-control2'}),
            'web': forms.TextInput(attrs={'class':'from-control2'}),
            'foto': forms.ClearableFileInput(attrs={'class':'from-co'}),
            'detalle': forms.TextInput(attrs={'class':'from-control2'}),
            }

class agregar_piloto_form(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = ['nombre','apellido','edad','genero','cedula','direccion','lugar_nacimiento','patrocinador','auto','web','foto','detalle']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'from-control2'}),
            'apellido': forms.TextInput(attrs={'class':'from-control2'}),
            'edad': forms.TextInput(attrs={'class':'from-control2'}),
            'genero': forms.TextInput(attrs={'class':'from-control2'}),
            'cedula': forms.TextInput(attrs={'class':'from-control2'}),
            'direccion': forms.TextInput(attrs={'class':'from-control2'}),
            'lugar_nacimiento': forms.TextInput(attrs={'class':'from-control2'}),
            'patrocinador': forms.Select(attrs={'class':'from-control2'}),
            'auto': forms.SelectMultiple(attrs={'class':'from-control3'}),
            'web': forms.TextInput(attrs={'class':'from-control2'}),
            'foto': forms.ClearableFileInput(attrs={'class':'from-co'}),
            'detalle': forms.TextInput(attrs={'class':'from-control2'}),
            }

class agregar_carrera_form(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre','lugar','fecha_inicio','fecha_final','competidores','foto','detalle']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'from-control2'}),
            'lugar': forms.TextInput(attrs={'class':'from-control2'}),
            'fecha_inicio': forms.TextInput(attrs={'class':'from-control2'}),
            'fecha_final': forms.TextInput(attrs={'class':'from-control2'}),
            'competidores': forms.SelectMultiple(attrs={'class':'from-control3'}),
            'foto': forms.ClearableFileInput(attrs={'class':'from-co'}),
            'detalle': forms.TextInput(attrs={'class':'from-control2'}),
            }

class login_form(forms.Form):
    usuario=forms.CharField(widget=forms.TextInput(attrs={"class":"from-control"}))
    clave=forms.CharField(widget=forms.PasswordInput(render_value=False,attrs={"class":"from-control"}))
    

class register_form(forms.Form):
    username  =forms.CharField(widget=forms.TextInput(attrs={"class":"from-control2"}))
    email  =forms.EmailField(widget=forms.TextInput(attrs={"class":"from-control2"}))
    password_1  =forms.CharField(label='password',widget=forms.PasswordInput(render_value=False,attrs={"class":"from-control2"}))
    password_2  =forms.CharField(label='comfirmar password',widget=forms.PasswordInput(render_value=False,attrs={"class":"from-control2"}))

    def clean_username(self):
        username=self.cleaned_data['username']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('nombre de usuario ya existe')


    def clean_email(self):
        email=self.cleaned_data['email']
        try:
            email = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('correo ya existe')

    def clean_password_2(self):
        password_1=self.cleaned_data['password_1']
        password_2=self.cleaned_data['password_2']

        if password_1==password_2:
            pass
        else:
            raise forms.ValidationError('password no coinciden')

class perfil_form(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto','identificacion']
        widgets = {
            
            'identificacion': forms.TextInput(attrs={'class':'from-control2'}),
            'foto': forms.ClearableFileInput(attrs={'class':'from-co'}),
            }


 
