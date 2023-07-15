import json
from django.db import models
from django.contrib.staticfiles.storage import staticfiles_storage
from .data.locations import get_locations
class CompanyDetails(models.Model):
    facebook_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    about = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    number1 = models.CharField(max_length=20, blank=True)
    number2 = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    open_and_closed_time = models.CharField(max_length=50, blank=True)
    open_and_closed_day = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.email


class AboutUs(models.Model):
    about_title = models.CharField(max_length=100)
    description = models.TextField()
    counter_name = models.CharField(max_length=50)
    counter_number = models.IntegerField()
    counter_name2 = models.CharField(max_length=50)
    counter_number2 = models.IntegerField()
    counter_name3 = models.CharField(max_length=50)
    counter_number3 = models.IntegerField()
    counter_name4 = models.CharField(max_length=50)
    counter_number4 = models.IntegerField()

    def __str__(self):
        return self.about_title


class Director(models.Model):
    image = models.ImageField(upload_to='directors/')
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    facebook_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name        


class Service(models.Model):
    image = models.ImageField(upload_to='services',blank=True, null=True)
    title = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100,blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    time = models.CharField(max_length=100,blank=True, null=True)
    service_name = models.CharField(max_length=100,blank=True, null=True)
    description = models.TextField(blank=True, null=True)        
    s_from = models.CharField(max_length=100,blank=True, null=True)
    s_to = models.CharField(max_length=100,blank=True, null=True)
    
    MENU_CHOICES = [
        ('Hourly Car Rental', 'Hourly Car Rental'),
        ('Daily Basis Rent A Car - Inside Dhaka', 'Daily Basis Rent A Car - Inside Dhaka'),
        ('Daily Basis Rent A Car - Outside Dhaka', 'Daily Basis Rent A Car - Outside Dhaka'),
        ('Monthly Car Rental', 'Monthly Car Rental'),
        ('Office Pick & Drop', 'Office Pick & Drop'),
        ('Inter District Pick&amp', 'Inter District Pick&amp'),
        ('Rent A Car in Sylhet', 'Rent A Car in Sylhet'),
        ('Rent A Car in Chittagong', 'Rent A Car in Chittagong'),
        ('Rent A Car in Cox s Bazar', 'Rent A Car in Cox s Bazar'),
        ('Rent A Car in Sajek Khagrachari', 'Rent A Car in Sajek Khagrachari'),
        ('Tour Package', 'Tour Package'),
    ]
    menu = models.CharField(max_length=255, choices=MENU_CHOICES)



    def __str__(self):
        return self.title 


class Package_title(models.Model):
    location = models.CharField(max_length=100)
    description = models.TextField()
    sub_menu_name = models.CharField(max_length=50)

    

    def __str__(self):
        return self.sub_menu_name 

class Package_car(models.Model):
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)
    car_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/')
    price = models.IntegerField()
    Car_Seats = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)

    MENU_CHOICES = [
        ('Airport Transfer', 'Airport Transfer'),
        ('Inter District Pick&Drop', 'Inter District Pick&Drop'),
        ('Rent A Car in Sylhet', 'Rent A Car in Sylhet'),
        ('Rent A Car in Chittagong', 'Rent A Car in Chittagong'),
        ("Rent A Car in Cox's Bazar", "Rent A Car in Cox's Bazar"),
        ('Day Tour Nearby Dhaka', 'Day Tour Nearby Dhaka'),
        ('Rent A Car in Sajek Khagracharii', 'Rent A Car in Sajek Khagrachari'),
        ('Tour Package', 'Tour Package'),
        ('Flexible Hourly Packages', 'Flexible Hourly Packages'),
    ]
    menu = models.CharField(max_length=255, choices=MENU_CHOICES)

    def __str__(self):
        return self.car_name      

class Pricing(models.Model):
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)
    car_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/')
    price = models.IntegerField()
    Car_Seats = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    
    
    divisions = []
    districts = []
    upazilas = []
    
    data = get_locations()


    divisions = sorted([(division['name'], division['name']) for division in data['divisions']])
    districts = sorted([(district['name'], district['name']) for district in data['districts']])
    upazilas = sorted([(upazila['name'], upazila['name']) for upazila in data['upazilas']])


    to_division = models.CharField(max_length=255, choices=divisions, blank=True, null=True)
    to_district = models.CharField(max_length=255, choices=districts, blank=True, null=True)
    to_upazila = models.CharField(max_length=255, choices=upazilas, blank=True, null=True)
    
    from_division = models.CharField(max_length=255, choices=divisions,blank=True, null=True)
    from_district = models.CharField(max_length=255, choices=districts,blank=True, null=True)
    from_upazila = models.CharField(max_length=255, choices=upazilas,blank=True, null=True)

    menu_choices = (
        ('Hourly Car Rental', 'Hourly Car Rental'),
        ('Daily Basis Rent A Car - Inside Dhaka', 'Daily Basis Rent A Car - Inside Dhaka'),
        ('Daily Basis Rent A Car - Outside Dhaka', 'Daily Basis Rent A Car - Outside Dhaka'),
        ('Monthly Car Rental', 'Monthly Car Rental'),
        ('Office Pick & Drop', 'Office Pick & Drop'),
    )
    menu = models.CharField(max_length=255, choices=menu_choices)    

    def __str__(self):
            return self.car_name  


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

class PickUp(models.Model):
    pick_name = models.CharField(max_length=150)
    price = models.IntegerField()
    location_from = models.CharField(max_length=550)
    location_to = models.CharField(max_length=550)
    location_to = models.CharField(max_length=550)
    load_capacity = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pickup_images/')
    description = models.TextField()

    menu_choices = (
        ('Package 1 ton', 'Package 1 ton'),
        ('Package 2 ton', 'package 2 ton'),
        ('Package 3 ton', 'package 3 ton'),
    )
    package_type = models.CharField(max_length=255, choices=menu_choices)
    class Meta:
        verbose_name = 'PickUp'
        verbose_name_plural = 'PickUp'

    def __str__(self):
        return self.pick_name
        
