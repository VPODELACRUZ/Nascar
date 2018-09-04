from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mecanico (models.Model):

    nombre           = models.CharField (max_length = 100)
    apellido         = models.CharField (max_length = 100)
    edad             = models.IntegerField()
    genero           = models.CharField (max_length = 100 )
    cedula           = models.IntegerField ()
    direccion        = models.CharField(max_length = 500)
    lugar_nacimiento = models.CharField(max_length = 500)
    web              = models.CharField(max_length = 500)
    foto             = models.ImageField(upload_to='mecanicos', null=True,blank=True)
    detalle          = models.CharField (max_length = 100,default=' ')





    def __str__ (self):
        return self.nombre


class Patrocinador (models.Model):

    nombre           = models.CharField (max_length = 100)
    telefono         = models.IntegerField()
    direccion        = models.CharField(max_length = 500)
    web              = models.CharField(max_length = 500)
    foto             = models.ImageField(upload_to='patrocinadores', null=True,blank=True)
    detalle          = models.CharField (max_length = 100,default=' ')


    def __str__ (self):
        return self.nombre



class Auto (models.Model):

    nombre           = models.CharField (max_length = 100)
    modelo           = models.IntegerField()
    marca            = models.CharField (max_length = 100)
    color            = models.CharField (max_length = 100 )
    precio           = models.DecimalField (max_digits = 14, decimal_places = 2 )
    cilindraje       = models.DecimalField (max_digits = 9, decimal_places = 2 )
    dimensiones      = models.CharField(max_length = 500)
    peso             = models.DecimalField (max_digits = 6, decimal_places = 2 )
    matricula        = models.CharField(max_length = 500)
    mecanico         = models.ManyToManyField(Mecanico, null = True, blank = True)
    foto             = models.ImageField(upload_to='autos', null=True,blank=True)
    detalle          = models.CharField (max_length = 100,default=' ')
   


    def __str__ (self):
        return self.nombre

class Piloto (models.Model):

    nombre           = models.CharField (max_length = 100)
    apellido         = models.CharField (max_length = 100)
    edad             = models.IntegerField()
    genero           = models.CharField (max_length = 100 )
    cedula           = models.IntegerField ()
    direccion        = models.CharField(max_length = 500)
    lugar_nacimiento = models.CharField(max_length = 500)
    patrocinador     = models.ForeignKey (Patrocinador, on_delete = models.PROTECT)
    auto             = models.ManyToManyField(Auto, null = True, blank = True)
    web              = models.CharField(max_length = 500)
    foto             = models.ImageField(upload_to='pilotos', null=True,blank=True)
    detalle          = models.CharField (max_length = 100,default=' ')



    def __str__ (self):
        return self.nombre


class Carrera (models.Model):

    nombre           = models.CharField (max_length = 100)
    lugar            = models.CharField(max_length = 500)
    fecha_inicio     = models.CharField(max_length = 500)
    fecha_final      = models.CharField(max_length = 500)
    competidores     = models.ManyToManyField(Piloto, null = True, blank = True)
    foto             = models.ImageField(upload_to='carreras', null=True,blank=True)
    detalle          = models.CharField (max_length = 100,default=' ')


    def __str__ (self):
        return self.nombre

class Perfil(models.Model):

    foto            = models.ImageField(upload_to='perfiles', null=True,blank=True)
    identificacion  = models.CharField(max_length = 100)
    user            = models.OneToOneField(User,on_delete=models.CASCADE)
    


    def __str__ (self):
        return self.identificacion


    
