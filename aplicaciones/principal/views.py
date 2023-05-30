from datetime import datetime
from django.shortcuts import redirect, render

from django.views.generic import *

from aplicaciones.libro.models import *

# Create your views here.


#pagina principal del proyecto
class Index(TemplateView):

    template_name = "principal/index.html"

    def dispatch(self, request, *args, **kwargs):

        """
        if request.user.is_anonymous:
            print("No estas autenticado, eres un usuario anonimo")
            return redirect("login:login")

        else:

            if request.user.has_perm('juegos.consultarjugada'):
                print("Entramos en ConsultarJugada")
            else:

                print("El usuario: ",request.user," no tiene acceso en ConsultarJugada")
                return redirect("principal:index")
        """
            

            
            #empresa_creada = Empresa.objects.filter(creado_por_id=request.user.id)


        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cantidad_libros = Libro.objects.all()

        #####Variables locales######
        pagado = 0

        por_vencer = 0 #Aqui colocamos el monto por vencer
        facturas_por_vencer = 0 #Aqui indicamos cuantas facturas estan por vencer

        vencido = 0
        facturas_vencidas = 0 #Aqui indicamos cuantas facturas estan vencidas

        ###########################

        #Para determinar la fecha del momento
        fecha_hoy = datetime.now().date() #Asi obtenemos la fecha actual



        #Vamos a calcular Pagado y todo lo demas
        for elemento in cantidad_libros:
            print(elemento)
            #Si la fecha de hoy es menor o igual a la fecha de cierre entonces verificamos la hora
            if fecha_hoy <= elemento.fecha_vencimiento:
                print("Aun no esta vencido")
                pagado +=elemento.monto_pagado
                por_vencer +=elemento.monto_pendiente
                facturas_por_vencer = facturas_por_vencer+1
            else:
                print("Esta factura esta vencida")
                pagado +=elemento.monto_pagado
                vencido+=elemento.monto_pendiente
                facturas_vencidas = facturas_vencidas+1

            #print("Monto Pagado: ",elemento.monto_pagado)
            #print("Monto Pendiente: ",elemento.monto_pendiente)



        context["pagado"] = pagado

        context["por_vencer"] = por_vencer
        context["facturas_por_vencer"] = facturas_por_vencer

        context["vencido"] = vencido
        context["facturas_vencidas"] = facturas_vencidas



        return context