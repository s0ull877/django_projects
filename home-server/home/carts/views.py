from django.http import HttpResponseRedirect
from django.shortcuts import render


from carts.models import HomeCart
from goods.models import Products


def basket_add_item(request, product_id):
    
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:

        carts = HomeCart.objects.filter(user=request.user, product=product)

        if carts.exists():

            cart = carts.last()
            cart.quantity += 1
            cart.save()
        
        else:

            HomeCart.objects.create(user=request.user,product=product)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_delete_item(request, cart_id):
    
    cart = HomeCart.objects.get(id=cart_id)
    cart.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])



def basket_change(request, product_id):
    pass