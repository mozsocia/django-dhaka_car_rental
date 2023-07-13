from django import template
from dashboard.models import *

register = template.Library()

@register.simple_tag
def get_packages():
    pachages = Package_car.objects.all()
    return pachages
