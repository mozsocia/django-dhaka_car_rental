from django.urls import path
from . views import *
from . import views


urlpatterns = [
    path('dashboard/admin/', dashboard, name='dashboard'),

    # slider
    # path('list', slider_list, name='list'),
    # path('create/',slider_create, name='create'),
    # path('update/<int:pk>/',slider_update, name='update'),
    # path('delete/<int:pk>/',slider_delete, name='delete'),


    # company_detail
    path('company_detail_list/', company_detail_list, name='company_detail_list'),
    path('company_detail_create/',company_detail_create, name='company_detail_create'),
    path('company_detail_update/<int:pk>/', company_detail_update, name='company_detail_update'),
    path('company_detail_delete/<int:pk>', company_detail_delete, name='company_detail_delete'),

    
    path('test/list/', test_list, name='test_list'),
    
    

    # about us
    path('about_us_list', about_us_list, name='about_us_list'),
    path('about_us_create/', about_us_create, name='about_us_create'),
    path('about_us_update/<int:pk>/', about_us_update, name='about_us_update'),
    path('about_us_delete/<int:pk>/', about_us_delete, name='about_us_delete'),

    # Pricing
    path('pricing_create/', pricing_create, name='pricing_create'),
    path('pricing_list/', pricing_list, name='pricing_list'),
    path('pricing_update/<int:pk>/', pricing_update, name='pricing_update'),
    path('pricing_delete/<int:pk>/', pricing_delete, name='pricing_delete'),
]




