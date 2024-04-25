from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from carts.utils import get_user_carts

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


@login_required
def create_order(request):
    
    user_carts = get_user_carts(request)
    user = request.user

    if request.method == 'POST':

        form = CreateOrderForm(data=request.POST)

        if form.is_valid():
            
            with transaction.atomic():
                if user_carts.exists():
                    
                    order = Order.objects.create(
                        user=user,
                        phone_number=form.cleaned_data['phone_number'],
                        requires_delivery=form.cleaned_data['requires_delivery'],
                        delivery_address=form.cleaned_data['delivery_address'],
                        payment_on_get=form.cleaned_data['payment_on_get'], 
                    )

                    for user_cart in user_carts:
                        product = user_cart.product
                        name = user_cart.product.name
                        price = user_cart.price
                        quantity = user_cart.quantity

                        if product.quantity < quantity:
                            raise ValidationError(f"Insufficient quantity of '{name}' in stock. \
                                                    In stock - {product.quantity}")
                        
                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            name=name,
                            price=price,
                            quantity=quantity,
                        )

                        product.quantity -= quantity
                        product.save()


                    user_carts.delete()

                    messages.success(request, 'Заказ оформлен!')
                    return redirect('users:profile', pk=user.id)
            
        else:
            context = {'title': 'Home - Новый заказ', 'form': form}

            return render(request, 'orders/create_order.html', context)


        
    elif request.method == 'GET':

        if not user_carts.exists():
            
            messages.warning(request, f"Вы не можете оформить заказ, пока корзина пуста!")

            return redirect(to='goods:catalog', slug='all')

        
        else:

            init = {
                'first_name': user.first_name,
                'last_name': user.last_name
            }

            form = CreateOrderForm(initial=init)

            context = {'title': 'Home - Новый заказ', 'form': form}

            return render(request, 'orders/create_order.html', context)
        