from django.urls import path,include
from django.contrib import admin
from mipagina.views import HomePageView,TecView,RegistrarView,VueloPageView,HospedajePageView,DescripViajesPageView,DescripVuelosPageView,DescripHospPageView,ViajeDeleteView,AboutPageView
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from orders.views import OrdersPageView, charge
#rutas para los templates 
urlpatterns = [
    path('admin/', admin.site.urls),
     path('accounts/', include('allauth.urls')),
    path('mipagina/', include('mipagina.urls')),
    path('orders/', include('orders.urls')),
    path('charge/', charge, name='charge'),
    path('orders/purchase',OrdersPageView.as_view(), name='orders'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('Home',HomePageView.as_view(), name='home'),
    path('', TemplateView.as_view(template_name='vuelo.html'), name='vuelo'),
    path('vuelo',VueloPageView.as_view(), name='vuelo'),
    path('', TemplateView.as_view(template_name='hospedaje.html'), name='hospedaje'),
    path('hospedaje',HospedajePageView.as_view(), name='hospedaje'),
    path('Acerca_de', TemplateView.as_view(template_name='About.html'), name='About'),
    path('Acerca_de',AboutPageView.as_view(), name='About'),
    path('Tec',TecView.as_view(), name='tec'),
    path('registrar/', RegistrarView.as_view(),name='registrar'),
    path('Descripcion/Viajes/<int:pk>',DescripViajesPageView.as_view(),name='DescViajes'),
    path('Descripcion/Vuelos/<int:pk>',DescripVuelosPageView.as_view(),name='DescVuelos'),
    path('Descripcion/Hospedajes/<int:pk>',DescripHospPageView.as_view(),name='DescHosp'),
    path('Viaje/<int:pk>/delete',ViajeDeleteView.as_view(),name='deleteViaje'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
