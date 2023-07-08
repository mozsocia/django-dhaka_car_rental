from django import forms
from dashboard.models import *



# class SliderForm(forms.ModelForm):
#     class Meta:
#         model = Slider
#         fields = '__all__'

class CompanyForm(forms.ModelForm):
    class Meta:
        model = CompanyDetails
        fields = '__all__'

class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = '__all__'