from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from .decorators import *
from .forms import *
from .models import *



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

# def register(request):
#     # Add your logic here
#     return render(request, 'main/pages/register.html')


from django.contrib.auth.models import User
from django.shortcuts import render, redirect


@guest_only
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            age = form.cleaned_data['age']
            phone = form.cleaned_data['phone']

            # Create a new user
            user = User.objects.create_user(username=username, password=password, email=email)

            # Create a profile for the user
            profile = Profile(user=user, full_name=full_name, age=age, phone=phone,)
            profile.save()

            # Redirect to login page or any other page after successful registration
            return redirect('login')


    return render(request, 'main/pages/register.html')



def login_user(request):
    error = None

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # User credentials are correct, log in the user
                login(request, user)
                # Redirect to a success page or any other page
                return redirect('home')
            else:
                # Invalid credentials, show an error message
                error = 'Invalid username or password.'

    return render(request, 'main/pages/login.html', {'error': error})    

