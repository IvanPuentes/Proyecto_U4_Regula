from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Hospedaje, Viaje, Vuelo, ComentarioVuelo,ComentarioViaje,ComentarioHosp
from .forms import UsuarioPersCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q, query
from django.contrib.auth.models import Permission



#vista de la pagina principal de viajes
class HomePageView(ListView):
    template_name = 'home.html'
    model = Viaje
    context_object_name='Listado'
    fields = 'ciudad','descrpicion','presio','img','noches',
#vista de la pagina principal de vuelos
class VueloPageView(ListView):
    template_name = 'vuelo.html'
    model = Vuelo
    context_object_name='Listado_vuelo'
    fields = 'ciudad','descrpicion','escala','presio','img',
#vista de la pagina principal de hospedaje
class HospedajePageView(ListView):
    template_name = 'hospedaje.html'
    model = Hospedaje
    context_object_name='Listado_hosp'
    fields = 'ciudad','beneficios','presio','img',
    
#vista de la pagina del tecnologico de la laguna
class TecView(ListView):
    template_name = 'Tec.html'
    model = Viaje
    context_object_name='Listado'

#vista de la pagina principal de acerca de 
class AboutPageView(ListView):
    template_name = 'About.html'
    model = Viaje
    context_object_name='Listado'

#vista de la pagina para registar nuevos usarios
class RegistrarView(CreateView):
   form_class = UsuarioPersCreationForm
   success_url = reverse_lazy('login')
   template_name = 'registrar.html'  

#vista de la pagina para la creacion de viajes
class CreateViajesView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
     model = Viaje
     success_url = reverse_lazy('home')
     template_name = "CreateViaje.html"
     fields = 'ciudad','descrpicion','presio','img','noches',
     context_object_name='Listado1'
     permission_required = ('mipagina.usuarioPerTot')
#vista de la pagina para la creacion de vuelos
class CreateVuelosView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
     model = Vuelo
     success_url = reverse_lazy('vuelo')
     template_name = "CreateVuelo.html"
     fields = 'ciudad','descrpicion','escala','presio','img',
     context_object_name='Listado1'
     permission_required = ('mipagina.usuariocomun')
     
 #vista de la pagina para la creacion de hospedajes   
class CreateHospedajeView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
     model = Hospedaje
     success_url = reverse_lazy('hospedaje')
     template_name = "CreateHospedaje.html"
     fields = 'ciudad','beneficios','presio','img',
     context_object_name='Listado1'
     permission_required = ('mipagina.add_access')

#vista de la pagina para editar los vuelos
class UpdatePageView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
     template_name = 'EditarViaje.html'
     model = Viaje
     success_url = reverse_lazy('home')
     fields = 'ciudad','descrpicion','presio','img','noches',
     permission_required = ('mipagina.usuarioPerTot')
#vista de la pagina para editar los viajes
class UpdateVueloPageView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
     template_name = 'EditarVuelo.html'
     model = Vuelo
     success_url = reverse_lazy('vuelo')
     fields = 'ciudad','descrpicion','escala','presio','img',
     permission_required = ('mipagina.usuariocomun')
    
#vista de la pagina para editar los hospedajes
class UpdateHospedajePageView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
     template_name = 'EditarHospedaje.html'
     model = Hospedaje
     success_url = reverse_lazy('hospedaje')
     fields = 'ciudad','beneficios','presio','img',
     permission_required = ('mipagina.add_access')


 
#vista de la pagina para describir los viajes
class DescripViajesPageView(LoginRequiredMixin,DetailView):
     template_name = 'DescViajes.html'
     model = Viaje
     context_object_name='Listado_viajes_des'
     fields = 'ciudad','descrpicion','presio','img','noches',
     login_url = 'login'
#vista de la pagina para describir los vuelos
class DescripVuelosPageView(LoginRequiredMixin,DetailView):
     template_name = 'DescVuelo.html'
     model = Vuelo
     context_object_name='Listado_viajes_des'
     fields = 'ciudad','descrpicion','escala','presio','img',
     login_url = 'login' 
#vista de la pagina para describir los hospedajes
class DescripHospPageView(LoginRequiredMixin,DetailView):
     template_name = 'DescHosp.html'
     model = Hospedaje
     context_object_name='Listado_viajes_des'
     fields = 'ciudad','beneficios','presio','img',
     login_url = 'login'  

#vista de la pagina para borrar los viajes
class ViajeDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
     template_name = 'deleteViajes.html'
     model = Viaje
     success_url = reverse_lazy('home')
     context_object_name='Autores'
     login_url = 'login'
     permission_required = ('mipagina.usuarioPerTot')

#vista de la pagina para borrar los viajes
class VueloDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
     template_name = 'deleteVueloS.html'
     model = Vuelo
     success_url = reverse_lazy('home')
     context_object_name='Autores'
     login_url = 'login'
     permission_required = ('mipagina.usuariocomun')
#vista de la pagina para borrar los viajes
class HospDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
     template_name = 'deleteHops.html'
     model = Hospedaje
     success_url = reverse_lazy('home')
     context_object_name='Autores'
     login_url = 'login'
     permission_required = ('mipagina.add_access')

#vista de la pagina de la creacion de comentarios
class ComentarioCreateView(LoginRequiredMixin,CreateView):
    model = ComentarioVuelo
    template_name = "comentarioNuevo.html"
    fields = ('comentario','Vuelo')
    login_url='login'
    success_url = reverse_lazy('home')
    context_object_name='Listado1'
#validacion para restringir la accion si no eres el usario que registro la creacion 
    def form_valid(self,form):
        form.instance.vuelo = Vuelo.objects.get(pk=self.kwargs.get('VueloComent'))
        return super().form_valid(form) 


#vista de la pagina de la creacion de comentarios
class ComentarioViajeCreateView(LoginRequiredMixin,CreateView):
    model = ComentarioViaje
    template_name = "comentarioNuevoV.html"
    fields = ('comentario','Viaje')
    login_url='login'
    success_url = reverse_lazy('home')
    context_object_name='Listado1'
#validacion para restringir la accion si no eres el usario que registro la creacion 
    def form_valid(self,form):
        form.instance.viaje = Viaje.objects.get(pk=self.kwargs.get('ViajeComent'))
        return super().form_valid(form) 


class ComentarioHospCreateView(LoginRequiredMixin,CreateView):
    model = ComentarioHosp
    template_name = "comentarioH.html"
    fields = ('comentario','Hospedaje')
    login_url='login'
    success_url = reverse_lazy('home')
    context_object_name='Listado1'
#validacion para restringir la accion si no eres el usario que registro la creacion 
    def form_valid(self,form):
        form.instance.hospedaje = Hospedaje.objects.get(pk=self.kwargs.get('HospComent'))
        return super().form_valid(form) 
    

class SearchResultListview(ListView):
    model = Vuelo
    context_object_name = 'listaBook'
    template_name = 'search_result.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        return Vuelo.objects.filter(
            Q(ciudad__icontains=query)
        )

