from django import template

from carts.models import HomeCart

register = template.Library()

@register.simple_tag()
def user_carts(request):
    
    if request.user.is_authenticated:
        return HomeCart.objects.filter(user=request.user)