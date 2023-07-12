from django import forms
from django.contrib.auth.models import User
from dashboard.models import ContactUs


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    
    full_name = forms.CharField(max_length=255)
    NID_number = forms.IntegerField()
    
    nid_image_front = forms.ImageField()
    nid_image_back = forms.ImageField()
    profile_image = forms.ImageField()





class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    # password = forms.CharField()

class ContactUsForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    message = forms.CharField()
    class Meta:
        model = ContactUs
        fields = '__all__'    