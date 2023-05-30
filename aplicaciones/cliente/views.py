from django.shortcuts import render
from django.views.generic import TemplateView

from aplicaciones.cliente.models import Clientes

# Create your views here.


#vista donde se vera la lista de los usuarios
class ListaClientes(TemplateView):

    template_name = "cliente/lista_clientes.html"

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
            


        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        listaClientes = Clientes.objects.all()
        context['listaClientes'] = listaClientes



        return context
