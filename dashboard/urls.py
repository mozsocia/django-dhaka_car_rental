from django.urls import path
from . views import *
from . import views


urlpatterns = [
    path('admin/dashboard/', dashboard, name='dashboard'),

    # slider
    # path('rrr', views.slider_list, name='list'),
    # path('create/', views.slider_create, name='create'),
    # path('update/<int:pk>/', views.slider_update, name='update'),
    # path('delete/<int:pk>/', views.slider_delete, name='delete'),

    path('create/', views.company_create, name='create'),
    path('company_detail/<int:pk>', views.company_detail, name='detail'),
    path('update/<int:pk>/update', views.company_update, name='update'),
    path('delete/<int:pk>', views.company_delete, name='delete'),

]