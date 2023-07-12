from django import forms
from django.contrib.auth.models import User
from dashboard.models import ContactUs


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    full_name = forms.CharField(max_length=255)
    phone = forms.IntegerField()
    
    nid_image = forms.ImageField()
    profile_image = forms.ImageField()


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField()

class ContactUsForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    message = forms.CharField()
    class Meta:
        model = ContactUs
        fields = '__all__'    