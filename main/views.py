from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def test(request):
    return render(request, 'test.html')

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