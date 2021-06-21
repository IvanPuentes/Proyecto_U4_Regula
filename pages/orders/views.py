from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
import stripe
from django.views.generic.base import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import Permission
from mipagina.models import Vuelo,Viaje,Hospedaje
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class OrdersPageView(DetailView):
    model = Vuelo
    context_object_name='Listado_viajes_des'
    fields = 'ciudad','descrpicion','escala','presio','img',
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key']=settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
    
    if request.method == 'POST':
        cantidad = request.POST["cantidad"]
        charge = stripe.Charge.create(
            amount = cantidad,
            currency='usd',
            description='pago de servicio',
            source=request.POST['stripeToken']
        )
    return render(request, 'orders/charge.html')



class OrdersViajePageView(DetailView):
    model = Viaje
    context_object_name='Listado_viajes_des'
    fields = 'ciudad','descrpicion','presio','img','noches',
    template_name = 'orders/purchaseViaje.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key']=settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
     
    if request.method == 'POST':
        cantidad = request.POST["cantidad"]
        charge = stripe.Charge.create(
            amount = cantidad,
            currency='usd',
            description='pago de servicio',
            source=request.POST['stripeToken']
        )
    return render(request, 'orders/charge.html')

        
class OrdersHospPageView(DetailView):
    model = Hospedaje
    context_object_name='Listado_viajes_des'
    fields = 'ciudad','descrpicion','presio','img','noches',
    template_name = 'orders/purchaseHosp.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key']=settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
     
    if request.method == 'POST':
        cantidad = request.POST["cantidad"]
        charge = stripe.Charge.create(
            amount = cantidad,
            currency='usd',
            description='pago de servicio',
            source=request.POST['stripeToken']
        )
    return render(request, 'orders/charge.html')

      