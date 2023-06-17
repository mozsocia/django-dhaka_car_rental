from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('test/', test, name='test'),
    
    
    # path('services/', service_list, name='service_list'),
    
    # path('slider/', views.slider_list, name='slider_list'),
    # path('slider/<int:slider_id>/', views.slider_detail, name='slider_detail'),
    
    
    # path('', views.car_list, name='car_list'),
    # path('car/<int:pk>/', views.car_detail, name='car_detail'),
    
    
    # path('packages/', views.package_list, name='package_list'),
    # path('packages/<int:pk>/', views.package_detail, name='package_detail'),


]
