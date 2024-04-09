from goods.models import Categories

class TitleMixin:
    title = None

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context


class CategoriesMixin:

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["categories"] = Categories.objects.all()
        return context
    