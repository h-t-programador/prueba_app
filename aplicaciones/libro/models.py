from django.db import models

from aplicaciones.cliente.models import Clientes

# Create your models here.

#Aqui se nombraran los tipos de documentos(Facturas, nota de credito, etc...)
class TipoDocumento(models.Model):
    
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField("Descripcion",max_length=200,unique=True)
    numero_documento = models.PositiveIntegerField(default=0)

    def __str__(self):
         return str(self.descripcion)+", numero de documento: "+str(self.numero_documento)

    class Meta:

        verbose_name = "Tipo de Documento"
        verbose_name_plural = "1.Tipo de Documento"

        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            
            #Permisos para iniciar y consultar jugadas

        ]#Fin de los permisos

#...(venta de giro, ventas que no son del giro)
class TipoVenta(models.Model):
    
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField("Descripcion",max_length=200,unique=True)
    numero_documento = models.PositiveIntegerField(default=0)

    def __str__(self):
         return str(self.descripcion)+", numero de documento: "+str(self.numero_documento)

    class Meta:

        verbose_name = "Tipo de Venta"
        verbose_name_plural = "2.Tipo Venta"

        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            
            #Permisos para iniciar y consultar jugadas

        ]#Fin de los permisos



#Aqui posiblemente cambiemos el nombre
class Libro(models.Model):

    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    #Tipo de documento puede ser(Factura, notaCredito, etc...)
    tipo_documento =  models.ForeignKey(TipoDocumento,on_delete=models.CASCADE,blank=True, null=True)
    #Desconozco aqui...
    tipo_venta = models.ForeignKey(TipoVenta,on_delete=models.CASCADE,blank=True, null=True)
    
    #NUMERO DE LA FACTURA(Se incrementa por cliente)
    folio = models.PositiveSmallIntegerField()

    #Fecha para hacer calculos pertinentes
    fecha_documento = models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)#Solo fecha
    
    #Podria llamarse hora recepcion
    hora_recepcion = models.TimeField (auto_now=False , auto_now_add=False )#Solo hora


    #EXENTA DE PAGAR IMPUESTOS(si esta en 0 es porque no hay IVA)
    monto_exento = models.PositiveIntegerField(default=0) 

    #MONTO BRUTO(MONTO TOTAL) = MONTO NETO + IMPUESTOS   
    monto_neto = models.PositiveIntegerField(default=0)    
    monto_iva = models.PositiveIntegerField(default=0)    

    #AQUI VA LA SUMA DE = MONTO NETO + IMPUESTOS
    monto_total = models.PositiveIntegerField(default=0)

    #Lo que falta por pagar
    monto_pendiente = models.PositiveIntegerField(default=0)

    #Lo que se ha pagado de esta factura
    monto_pagado = models.PositiveIntegerField(default=0)

    #En algunos tipos de documentos estos valores se anula
    fecha_vencimiento = models.DateField()

    def __str__(self):
         return str(self.cliente.razon_social)+", "+str(self.tipo_documento.descripcion)+", Folio numero:"+str(self.folio)

    class Meta:

        verbose_name = "Libro"
        verbose_name_plural = "3.Libros"

        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            
            #Permisos para iniciar y consultar jugadas

        ]#Fin de los permisos



#Con este modelo pagamos la factura por parte o completo
class ConciliacionPagos(models.Model):
    
	
    # Falta indicar relacion con tabla Factura
    factura = models.ForeignKey(Libro, on_delete=models.CASCADE,blank=True, null=True)

    #NUMERO DE LA FACTURA(Se incrementa por cliente)
    numero_registro = models.PositiveSmallIntegerField()
    fecha_de_Pago = models.DateField()
    monto_pagado = models.PositiveIntegerField()
    fecha_conciliacion = models.DateField()

    def __str__(self):
         return str(self.factura)+" "+str(self.numero_registro)
    

    class Meta:

        verbose_name = "ConciliacionPago"
        verbose_name_plural = "4.ConciliacionPagos"

        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            
            #Permisos para iniciar y consultar jugadas

        ]#Fin de los permisos
	


