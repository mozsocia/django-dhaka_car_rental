from django.shortcuts import render
from .models import *

from django.shortcuts import render, get_object_or_404, redirect
# from .forms import CompanyForm
# from .models import CompanyDetails

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/pages/dashboard.html')


# Company Details 

# def company_create(request):
#     if request.method == 'POST':
#         form = CompanyForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('company_detail', pk=form.instance.pk)
#     else:
#         form = CompanyForm()
#     return render(request, 'company/create.html', {'form': form})

# def company_detail(request, pk):
#     company = get_object_or_404(CompanyDetails, pk=pk)
#     return render(request, 'company/detail.html', {'company': company})

# def company_update(request, pk):
#     company = get_object_or_404(CompanyDetails, pk=pk)
#     if request.method == 'POST':
#         form = CompanyForm(request.POST, instance=company)
#         if form.is_valid():
#             form.save()
#             return redirect('company_detail', pk=company.pk)
#     else:
#         form = CompanyForm(instance=company)
#     return render(request, 'company/update.html', {'form': form, 'company': company})

# def company_delete(request, pk):
#     company = get_object_or_404(CompanyDetails, pk=pk)
#     if request.method == 'POST':
#         company.delete()
#         return redirect('company_list')
#     return render(request, 'company/delete.html', {'company': company})


