from django import template
from dashboard.models import *

register = template.Library()

@register.simple_tag
def get_packages():
    pachages = Package_car.objects.all()
    menu_choices = [
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
    return menu_choices
