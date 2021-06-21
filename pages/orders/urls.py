from django.urls import path
from django.urls import path
from orders.views import OrdersPageView, charge,OrdersViajePageView,OrdersHospPageView

urlpatterns=[
    path('charge/', charge, name='charge'),
    path('orders/purchase/<int:pk>',OrdersPageView.as_view(), name='orders'),
    path('orders_viaje/purchase/<int:pk>',OrdersViajePageView.as_view(), name='orders_viaje'),
    path('orders_hosp/purchase/<int:pk>',OrdersHospPageView.as_view(), name='orders_hosp'),
    
]