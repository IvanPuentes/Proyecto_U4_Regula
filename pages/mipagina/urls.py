from django.urls import path,include
from .views import HomePageView,TecView,RegistrarView,CreateViajesView,CreateVuelosView,VueloPageView,CreateHospedajeView,HospedajePageView,UpdatePageView,UpdateVueloPageView,UpdateHospedajePageView,DescripViajesPageView,DescripVuelosPageView,DescripHospPageView,ViajeDeleteView,AboutPageView,ComentarioCreateView,SearchResultListview,VueloDeleteView,HospDeleteView,ComentarioViajeCreateView,ComentarioHospCreateView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
#importar las librerias y los archivos 

#rutas para los templates 

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('Vuelos',VueloPageView.as_view(),name='vuelo'),
    path('Hospedaje',HospedajePageView.as_view(),name='hospedaje'),
     path('orders/', include('orders.urls')),
    path('Acerca_de',AboutPageView.as_view(), name='About'),
    path('registrar/', RegistrarView.as_view(),name='registrar'),
    path('Nuevo/Viaje',CreateViajesView.as_view(),name='CreateViaje'),
    path('Nuevo/Vuelo',CreateVuelosView.as_view(),name='CreateVuelo'),
    path('Nuevo/Hospedaje',CreateHospedajeView.as_view(),name='CreateHospedaje'),
    path('Viajes/<int:pk>/Update',UpdatePageView.as_view(),name='EditarViaje'),
    path('Vuelo/<int:pk>/Update',UpdateVueloPageView.as_view(),name='EditarVuelo'),
    path('Hospedaje/<int:pk>/Update',UpdateHospedajePageView.as_view(),name='EditarHospedaje'),
    path('Descripcion/Viajes/<int:pk>',DescripViajesPageView.as_view(),name='DescViajes'),
    path('Descripcion/Vuelos/<int:pk>',DescripVuelosPageView.as_view(),name='DescVuelos'),
    path('Descripcion/Hospedaje/<int:pk>',DescripHospPageView.as_view(),name='DescHosp'),
    path('Viaje/<int:pk>/delete',ViajeDeleteView.as_view(),name='deleteViaje'),
    path('Vuelo/<int:pk>/delete',VueloDeleteView.as_view(),name='deleteVuelo'),
    path('Hospedaje/<int:pk>/delete',HospDeleteView.as_view(),name='deleteHosp'),
    path('Tec',TecView .as_view(),name='tec'),
    path('Comentarios/<int:VueloComent>',ComentarioCreateView.as_view(),name='comentarioNuevo'),
    path('ComentariosViaje/<int:ViajeComent>',ComentarioViajeCreateView.as_view(),name='comentarioNuevoV'),
    path('ComentariosHosp/<int:HospComent>',ComentarioHospCreateView.as_view(),name='comentarioH'),
    path('search', SearchResultListview.as_view(), name='search_result'),

    #rutas para los cambios y reset de contraseñas 
    path('password_reset/', PasswordResetView.as_view(
        template_name='registration/password_reset.html'
    ),name='password_reset'),

    path('password_reset_done/', PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ),name='password_reset_done'),

    path('usuarios/password_reset_confirm/<u1db64>/<token>', PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ),name='password_reset_confirm'),

    path('usuarios/password_reset_complete', PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ),name='password_reset_complete'),

]
