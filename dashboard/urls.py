from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('hhh', dashboard, name='dashboard'),


    # path('create/', views.company_create, name='create'),
    # path('<int:pk>/', views.company_detail, name='detail'),
    # path('<int:pk>/update/', views.company_update, name='update'),
    # path('<int:pk>/delete/', views.company_delete, name='delete'),

]