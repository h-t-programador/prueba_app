from django.db import models

# Create your models here.


class Empresa(models.Model):

    #
    id = models.AutoField(primary_key=True)

    #Nombre de la empresa...
    razon_social = models.CharField(max_length=255, null=True, blank=True)
    rut = models.CharField("Rut",max_length=20,unique=True,null=True,blank=True)#Esto es como id de la cedula
    direccion = models.CharField("Direccion",max_length=100,blank=True, null=True,default="Desconocido") 
    contacto = models.CharField("Contacto",max_length=50,null=True,blank=True)
    correo = models.EmailField("Correo Electronico",max_length=150, unique=True)
    telefono = models.CharField("Telefono",max_length=20,null=True,blank=True)

    def __str__(self):
         return str(self.razon_social)+", rut: "+str(self.rut)

    class Meta:

        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            
            #Permisos para iniciar y consultar jugadas
        ]