"""Book View Module."""
from django.views.generic import TemplateView



class BookView(TemplateView):
    """BookView."""
    template_name = 'book/index.html'
