from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def service(request):
    return render(request, 'pages/service.html')

def contact(request):
    return render(request, 'pages/contact.html')

def pricing(request):
    return render(request, 'pages/pricing.html')

def pickup(request):
    return render(request, 'pages/pickup.html')



def package(request):
    return render(request, 'pages/package.html')

def test(request):
    return render(request, 'pages/test.html')


# ----------------------------------------------------------------
# information pages
def information(request):
    return render(request, 'pages/information/index.html')

def our_cars_view(request):
    # Add your logic here
    return render(request, 'pages/information/our_cars.html')

def our_clients_view(request):
    # Add your logic here
    return render(request, 'pages/information/our_clients.html')

def city_distance_view(request):
    # Add your logic here
    return render(request, 'pages/information/city_distance.html')

def terms_conditions_view(request):
    # Add your logic here
    return render(request, 'pages/information/terms_conditions.html')

def privacy_policy_view(request):
    # Add your logic here
    return render(request, 'pages/information/privacy_policy.html')

def faqs_view(request):
    # Add your logic here
    return render(request, 'pages/information/faqs.html')

# def service_list(request):
#     services = Service.objects.all()
#     return render(request, 'service_list.html', {'services': services})


# def slider_list(request):
#     sliders = Slider.objects.all()
#     return render(request, 'slider/slider_list.html', {'sliders': sliders})

# def slider_detail(request, slider_id):
#     slider = get_object_or_404(Slider, pk=slider_id)
#     return render(request, 'slider/slider_detail.html', {'slider': slider})


# def car_list(request):
#     cars = Car.objects.all()
#     return render(request, 'cars/car_list.html', {'cars': cars})

# def car_detail(request, pk):
#     car = get_object_or_404(Car, pk=pk)
#     return render(request, 'cars/car_detail.html', {'car': car})


# def package_list(request):
#     packages = Package.objects.all()
#     return render(request, 'package_list.html', {'packages': packages})

# def package_detail(request, pk):
#     package = get_object_or_404(Package, pk=pk)