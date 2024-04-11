from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from common.views import TitleMixin

from goods.models import Products, Categories



class ProductsListView(TitleMixin, ListView):

    model = Products
    template_name = "goods/catalog.html"
    title = 'Home - Каталог'
    paginate_by = 3


    def get_context_data(self, **kwargs) -> dict:
        
        context = super().get_context_data(**kwargs)
        return context

    
    def get_queryset(self):

        queryset = super().get_queryset()
        
        slug = self.kwargs['slug']
        products = Categories.objects.get(slug=slug).products_set.all().order_by('id')
        
        params = self.request.GET
        if params.get('on_sale'):
            products = products.filter(discount__gt=0)

        if params.get('order_by'):
            products = products.order_by(params.get('order_by'))

        return products
    


class ProductDetailView(TitleMixin, DetailView):

    model = Products
    template_name = "goods/product.html"
    title = 'Home - Продукт'


    




