from django.urls import path
from .views import *
from . import *


urlpatterns = [
    path('hhh', index, name='index'),

]