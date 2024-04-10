from django.shortcuts import render
from django.views.generic.list import ListView

from common.views import TitleMixin, CategoriesMixin

from goods.models import Products, Categories



class ProductsListView(TitleMixin, CategoriesMixin, ListView):

    model = Products
    template_name = "goods/catalog.html"
    title = 'Home - Каталог'

    def get_context_data(self, **kwargs) -> dict:
        
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        products = Categories.objects.get(slug=slug).products_set.all()
        context['products'] = products
        return context
    





def product(request):
    return render(request, 'goods/product.html')