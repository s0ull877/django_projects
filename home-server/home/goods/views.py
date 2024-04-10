from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from common.views import TitleMixin, CategoriesMixin

from goods.models import Products, Categories



class ProductsListView(TitleMixin, CategoriesMixin, ListView):

    model = Products
    template_name = "goods/catalog.html"
    title = 'Home - Каталог'
    paginate_by = 6


    # def get_context_data(self, **kwargs) -> dict:
        
    #     context = super().get_context_data(**kwargs)
    #     slug = self.kwargs['slug']
    #     products = Categories.objects.get(slug=slug).products_set.all()
    #     context['products'] = products
    #     return context

    
    def get_queryset(self):

        queryset = super().get_queryset()
        slug = self.kwargs['slug']
        products = Categories.objects.get(slug=slug).products_set.all().order_by('id')

        return products
    


class ProductDetailView(TitleMixin, CategoriesMixin, DetailView):

    model = Products
    template_name = "goods/product.html"
    title = 'Home - Продукт'


    




