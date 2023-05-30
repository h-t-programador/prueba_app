from django.db import models

from aplicaciones.empresa.models import Empresa

# Create your models here.


#modelo de los usuarios
class Clientes(models.Model):

    #
    id = models.AutoField(primary_key=True)

    #Empresa a la que pertenezco
    
    #aqui la razon social, es la empresa a la que esta asociada el cliente
    #razon_social = models.ForeignKey(Empresa, on_delete=models.CASCADE,blank=True, null=True)
    razon_social = models.CharField("Razon Social",max_length=255,unique=True,null=True,blank=True)
    rut = models.CharField("Rut",max_length=20,unique=True,null=True,blank=True)#Esto es como id de la cedula
    direccion = models.CharField("Direccion",max_length=100,blank=True, null=True,default="Desconocido") 
    contacto = models.CharField("Contacto",max_length=50,null=True,blank=True)
    correo = models.EmailField("Correo Electronico",max_length=150, unique=True)
    telefono = models.CharField("Telefono",max_length=20,null=True,blank=True)

    #Para verificar si esta activo o no
    activo = models.BooleanField(default=True)

    def __str__(self):
         return str(self.razon_social)+", rut: "+str(self.rut)

    class Meta:

        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            
            #Permisos para iniciar y consultar jugadas
        ]
