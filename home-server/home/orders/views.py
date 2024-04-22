from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from carts.utils import get_user_carts


@login_required
def create_order(request):
    
    user_carts = get_user_carts(request)

    if not user_carts.exists():
        
        messages.warning(request, f"Вы не можете оформить заказ, пока корзина пуста!")

        return HttpResponseRedirect(reverse('goods:catalog', kwargs={'slug':'all'}))
    
    else:

        context = {'title': 'Home - Новый заказ'}

        return render(request, 'orders/create_order.html', context)