from django.shortcuts import render
from dashboard.models import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from .decorators import *
from .forms import *
from .models import *
from django.db import transaction
from pprint import pprint

from django.contrib.auth import logout


def home(request):
    car = Pricing.objects.all()
    return render(request, 'main/pages/index.html',{'car':car})

def about(request):
    director = Director.objects.all()
    about = AboutUs.objects.all()
    context ={
        'director':director,
        'about':about
    }
    return render(request, 'main/pages/about.html',context)

def service(request):
    return render(request, 'main/pages/service.html')

def contact(request):
    return render(request, 'main/pages/contact.html')

def pricing(request):
    pricing = Pricing.objects.all()

    return render(request, 'main/pages/pricing.html',{'pricing': pricing})
    
def pickup(request):
    return render(request, 'main/pages/pickup.html')



def package(request):
    package = Package_car.objects.all()
    return render(request, 'main/pages/package.html',{'package': package})

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



# def login(request):
#     # Add your logic here
#     return render(request, 'main/pages/login.html')

def profile(request):
    profile = FrontProfile.objects.all()
    

    context ={
        'profile':profile
    }

    return render(request, 'main/pages/profile.html',context)


from django.contrib.auth.models import User
from django.shortcuts import render, redirect


@guest_only
@transaction.atomic
def register(request):
    normal_error = {}
    form_error = None
    
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            phone = form.cleaned_data['phone']
            
            nid_image = form.cleaned_data['nid_image']
            profile_image = form.cleaned_data['profile_image']



            try:
                # Create a new user
                user = User.objects.create_user(username=username, password=password, email=email)

                # Create a profile for the user
                profile = FrontProfile.objects.create(user=user, full_name=full_name,phone=phone,nid_image=nid_image, profile_image=profile_image )

                # Redirect to login page or any other page after successful registration
                return redirect('login_user')
            
            except Exception as e:
                if 'UNIQUE constraint failed: auth_user.username' in str(e):
                    normal_error['username'] = "Username already in use"
                
                    
                # pprint(str(e))
                # pprint(normal_error)
                # Handle the exception and display an error message
                # messages.error(request, f"An error occurred: {str(e)}")
            
        else:
            form_error = form.errors
            pprint(form_error)
            

    return render(request, 'main/pages/register.html', {'form_error': form_error, 'normal_error': normal_error } )


@guest_only
def login_user(request): 
    form_error = None
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

        else:
            form_error = form.errors
            # pprint(form_error)            

    return render(request, 'main/pages/login.html', {'form_error': form_error})    



def logout_user(request):

    logout(request)
    
    return redirect('home')  # Replace 'home' with the appropriate URL name
    

#  CKEditor
def my_model_list(request):
    my_models = MyModel.objects.all()
    return render(request, 'my_model_list.html', {'my_models': my_models})

def my_model_create(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        MyModel.objects.create(content=content)
        return redirect('my_model_list')
    return render(request, 'my_model_create.html')
