from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404



def home(request):
    return render(request, 'main/pages/index.html')

def about(request):
    return render(request, 'main/pages/about.html')

def service(request):
    return render(request, 'main/pages/service.html')

def contact(request):
    return render(request, 'main/pages/contact.html')

def pricing(request):
    return render(request, 'main/pages/pricing.html')

def pickup(request):
    return render(request, 'main/pages/pickup.html')



def package(request):
    return render(request, 'main/pages/package.html')

def test(request):
    return render(request, 'main/pages/test.html')


# ----------------------------------------------------------------
# information pages
def information(request):
    return render(request, 'main/pages/information/index.html')

def our_cars_view(request):
    # Add your logic here
    return render(request, 'main/pages/information/our_cars.html')

def our_clients_view(request):
    # Add your logic here
    return render(request, 'main/pages/information/our_clients.html')

def city_distance_view(request):
    # Add your logic here
    return render(request, 'main/pages/information/city_distance.html')

def terms_conditions_view(request):
    # Add your logic here
    return render(request, 'main/pages/information/terms_conditions.html')

def privacy_policy_view(request):
    # Add your logic here
    return render(request, 'main/pages/information/privacy_policy.html')

def faqs_view(request):
    # Add your logic here
    return render(request, 'main/pages/information/faqs.html')


def login(request):
    # Add your logic here
    return render(request, 'main/pages/login.html')

def register(request):
    # Add your logic here
    return render(request, 'main/pages/register.html')

