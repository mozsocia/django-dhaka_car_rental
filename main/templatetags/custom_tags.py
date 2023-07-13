from django import template
from dashboard.models import CompanyDetails

register = template.Library()

@register.simple_tag
def get_details():
    details = CompanyDetails.objects.all()
    return details