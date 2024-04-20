from carts.models import HomeCart

def get_user_carts(request):

    if request.user.is_authenticated:
        return HomeCart.objects.filter(user=request.user)