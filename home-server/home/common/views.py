
class TitleMixin:
    title = None

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context
    