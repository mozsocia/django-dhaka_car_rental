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
    path('login_user/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_user, name='logout'),
    # path('update_profile/', update_profile, name='update_profile'),

    

    
]
