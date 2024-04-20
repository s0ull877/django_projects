from django.urls import path

from carts.views import basket_add_item, basket_change, basket_delete_item

app_name = 'carts'

urlpatterns = [
    path('basket_add/<int:product_id>/', basket_add_item, name='add'),
    path('basket_delete/<int:cart_id>/', basket_delete_item, name='delete'),
    path('basket_change/<int:product_id>/', basket_change, name='change'),
]
