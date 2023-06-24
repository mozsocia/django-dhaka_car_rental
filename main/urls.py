from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('test/', test, name='test'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('contact/', contact, name='contact'),
    path('pricing/',pricing, name='princing'),
    path('pickup/', pickup, name='pickup'),
    
    path('information/', information, name='information'),
    path('information/our-cars/', views.our_cars_view, name='our-cars'),
    path('information/our-clients/', views.our_clients_view, name='our-clients'),
    path('information/city-distance/', views.city_distance_view, name='city-distance'),
    path('information/terms-and-conditions/', views.terms_conditions_view, name='terms-conditions'),
    path('information/privacy-policy/', views.privacy_policy_view, name='privacy-policy'),
    path('information/faqs/', views.faqs_view, name='faqs'),
    
    
    path('package/', package, name='package'),

    
    
    
    
    # path('services/', service_list, name='service_list'),
    
    # path('slider/', views.slider_list, name='slider_list'),
    # path('slider/<int:slider_id>/', views.slider_detail, name='slider_detail'),
    
    
    # path('', views.car_list, name='car_list'),
    # path('car/<int:pk>/', views.car_detail, name='car_detail'),
    
    
    # path('packages/', views.package_list, name='package_list'),
    # path('packages/<int:pk>/', views.package_detail, name='package_detail'),


]
