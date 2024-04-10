from django.urls import path

from goods.views import ProductsListView, product

app_name = 'goods'

urlpatterns = [
    path('<slug:slug>/', ProductsListView.as_view(), name='catalog'),
    path('product/', product, name='product'),

]
