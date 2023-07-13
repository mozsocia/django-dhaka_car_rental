from django import template
from dashboard.models import *

register = template.Library()

@register.simple_tag
def get_services():
    services = Service.objects.all()
    return services
