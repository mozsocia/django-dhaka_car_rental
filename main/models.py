from django.db import models

# Create your models here.


# class Service(models.Model):
#     submenu_name = models.CharField(max_length=100)
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.submenu_name
    
    
    
# class Slider(models.Model):
#     image = models.ImageField(upload_to='slider_images/')
#     title = models.CharField(max_length=100)
#     subtitle = models.CharField(max_length=100)
#     title_attribute = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
    
    
    
    
# class Car(models.Model):
#     name = models.CharField(max_length=100)
#     # price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     image = models.ImageField(upload_to='car_images')
#     specifications = models.JSONField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
    
# class Package(models.Model):
#     title = models.CharField(max_length=100)
#     details = models.JSONField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)




# class Package(models.Model):
#     title = models.CharField(max_length=100)
#     details = models.TextField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     car_name = models.CharField(max_length=100)
#     car_description = models.TextField()
#     car_image = models.ImageField(upload_to='car_images/')
#     car_specifications = models.TextField()

#     def get_car_specifications(self):
#         return self.car_specifications.split(',')

#     def set_car_specifications(self, specifications):
#         self.car_specifications = ','.join(specifications)

#     def __str__(self):
#         return self.title


# class CarList(models.Model):
#     name = models.CharField(max_length=256)
#     category = models.CharField(max_length=256) 
#     body_style = models.CharField(max_length=256)
#     number_of_seats = models.IntegerField()