from django.shortcuts import render
from dashboard.models import *
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *


# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/pages/dashboard.html')

# slider

def slider_list(request):
    sliders = Slider.objects.all()
    return render(request, 'dashboard/pages/slider/list.html', {'sliders': sliders})

def slider_create(request):
    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('slider:list')
    else:
        form = SliderForm()
    return render(request, 'dashboard/pages/slider/create.html', {'form': form})

def slider_update(request, pk):
    slider = get_object_or_404(Slider, pk=pk)
    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES, instance=slider)
        if form.is_valid():
            form.save()
            return redirect('slider:list')
    else:
        form = SliderForm(instance=slider)
    return render(request, 'dashboard/pages/slider/create.html', {'form': form})


def slider_delete(request,pk):
    slider=Slider.objects.get(pk=pk)
    banner.delete()
    return redirect('slider-list')




# Company Details 

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_detail', pk=form.instance.pk)
    else:
        form = CompanyForm()
    return render(request, 'dashboard/pages/company/create.html', {'form': form})

def company_detail(request, pk):
    company = get_object_or_404(CompanyDetails, pk=pk)
    return render(request, 'dashboard/pages/company/detail.html', {'company': company})

def company_update(request, pk):
    company = get_object_or_404(CompanyDetails, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_detail', pk=company.pk)
    else:
        form = CompanyForm(instance=company)
    return render(request, 'dashboard/pages/company/update.html', {'form': form, 'company': company})


def company_delete(request,pk):
    company=CompanyDetails.objects.get(pk=pk)
    company.delete()
    return redirect('company_list')    


# banner

def banner_list(request):
    banner_list = BannerSlider.objects.all().order_by('-id')
    return render(request, 'dashboard/banner/list.html', {'banner_list':banner_list})

def banner_add(request):
    if request.method == 'POST':
        form = BannerSliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('banner-list')
    else:
        form = BannerSliderForm()
    return render(request, 'dashboard/banner/add.html', {'form':form})

def banner_edit(request,pk):
    banner = BannerSlider.objects.get(pk=pk)
    if request.method == 'POST':
        form = BannerSlideForm(request.POST,request.FILES,instance=banner)
        if form.is_valid():
            form.save()
            return redirect('banner-list') 
        else:
            return redirect('banner-add')
    else:
        form = BannerSlideForm(instance=banner)
    return render(request, 'dashboard/banner/add.html', {'form':form})


def banner_delete(request,pk):
    banner=BannerSlider.objects.get(pk=pk)
    banner.delete()
    messages.success(request, 'Successfully delete')
    return redirect('banner-list')