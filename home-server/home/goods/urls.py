from django.urls import path

from goods.views import ProductsListView, ProductDetailView

app_name = 'goods'

urlpatterns = [
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('<slug:slug>/', ProductsListView.as_view(), name='catalog'),

]
