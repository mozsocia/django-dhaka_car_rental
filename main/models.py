from django.db import models

class Slider(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    textone = models.CharField(max_length=100)
    texttwo = models.CharField(max_length=100)
    textthree = models.CharField(max_length=100)