from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model



# Create your models here.

#modelo del usario personalizado del proyecto final
class UsuarioPers(AbstractUser):
    edad = models.PositiveIntegerField(null=True, blank=True)
    telefono = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    genero = models.CharField(null=True,blank=True, max_length=1)
    
    

#se presntan los diferentes modelos de la base de datos diseñada en posgres 
#modelo de las ciudades 
class Ciudad(models.Model):
    nombre = models.TextField(default="")
    
    def __str__(self):
        return self.nombre

#modelo de hospedaje en la base de datos 
class Hospedaje(models.Model):
    ciudad = models.TextField(default="")
    beneficios = models.TextField(default="")
    presio = models.TextField(default="")
    img =models.ImageField(null=True, blank=True, upload_to="images/")
  
    class Meta:
        permissions = [
            ('add_access','Permite agregar registros'),
        ]

    def __str__(self):
        return self.ciudad

    def get_absolute_url(self):
        return reverse('', args=[str(self.id)])

#modelo de vuelo en la base de datos 
class Vuelo(models.Model):
    ciudad = models.TextField(default="")
    descrpicion = models.TextField(default="")
    escala = models.TextField(default="")
    presio = models.TextField(default="")
    img = models.ImageField(null=True, blank=True, upload_to="images/")
    
    class Meta:
        permissions = [
            ('usuariocomun','Permite a los usarios agregar,editar,eliminar'),
        ]
    
    def __str__(self):
        return self.ciudad

    def get_absolute_url(self):
        return reverse('', args=[str(self.id)])

#modelo de viaje en la base de datos 
class Viaje(models.Model):
    ciudad = models.TextField(default="")
    descrpicion = models.TextField(default="")
    presio = models.TextField(default="")
    img = models.ImageField(null=True, blank=True, upload_to="images/")
    noches = models.TextField(default="")

    class Meta:
            permissions = [
                ('usuarioPerTot','Permite a los usarios agregar,editar,eliminar en modelo viaje'),
            ]
    def __str__(self):
        return self.ciudad

    def get_absolute_url(self):
        return reverse('', args=[str(self.id)])


#modelo de los comentarios  agregando dos llaves foraneas para los autores y los usarios
class ComentarioVuelo(models.Model):
    comentario = models.TextField(default="")
    Vuelo = models.ForeignKey(
        Vuelo,
        default="",
        on_delete= models.CASCADE,
    )
        
    def __str__(self):
        return self.comentario
    
class ComentarioViaje(models.Model):
    comentario = models.TextField(default="")
    Viaje = models.ForeignKey(
        Viaje,
        default="",
        on_delete= models.CASCADE,
    )
        
    def __str__(self):
        return self.comentario
    

class ComentarioHosp(models.Model):
    comentario = models.TextField(default="")
    Hospedaje = models.ForeignKey(
        Hospedaje,
        default="",
        on_delete= models.CASCADE,
    )
    

    def __str__(self):
        return self.comentario
    
