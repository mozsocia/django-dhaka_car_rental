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
        return self.title


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