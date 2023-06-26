from django import forms
from main.models import *



# class SliderForm(forms.ModelForm):
#     class Meta:
#         model = Slider
#         fields = '__all__'

class CompanyForm(forms.ModelForm):
    class Meta:
        model = CompanyDetails
        fields = '__all__'