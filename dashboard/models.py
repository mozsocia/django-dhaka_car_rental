from django.db import models



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

    def __str__(self):
        return self.name        


class Service(models.Model):
    image = models.ImageField(upload_to='services')
    title = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    body = models.TextField()
    time = models.CharField(max_length=100)
    service_name = models.CharField(max_length=100)
    description = models.TextField()        

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
    price = models.DecimalField(max_digits=8, decimal_places=2)
    Car_Seats = models.DecimalField(max_digits=8, decimal_places=2)
    car_type = models.CharField(max_length=100)

    MENU_CHOICES = [
        ('airport_transfer', 'Airport Transfer'),
        ('inter_district_pick_drop', 'Inter District Pick&Drop'),
        ('rent_car_sylhet', 'Rent A Car in Sylhet'),
        ('rent_car_chittagong', 'Rent A Car in Chittagong'),
        ('rent_car_cox_bazar', "Rent A Car in Cox's Bazar"),
        ('day_tour_dhaka', 'Day Tour Nearby Dhaka'),
        ('rent_car_sajek_khagrachari', 'Rent A Car in Sajek Khagrachari'),
        ('tour_package', 'Tour Package'),
        ('hourly_packages', 'Flexible Hourly Packages'),
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
    price = models.DecimalField(max_digits=8, decimal_places=2)
    Car_Seats = models.DecimalField(max_digits=8, decimal_places=2)
    car_type = models.CharField(max_length=100)



    menu_choices = (
        ('hourly', 'Hourly Car Rental'),
        ('daily_dhaka', 'Daily Basis Rent A Car - Inside Dhaka'),
        ('daily_outside', 'Daily Basis Rent A Car - Outside Dhaka'),
        ('monthly', 'Monthly Car Rental'),
        ('pick_drop', 'Office Pick & Drop'),
    )
    menu = models.CharField(max_length=255, choices=menu_choices)    

    def __str__(self):
            return self.car_name  