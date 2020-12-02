"""Book API view module."""
from wisatabook.models import Book
from api.serializers import BookSerializer

from rest_framework import decorators, viewsets, filters
from api.services.book import book_service
from django.http import JsonResponse


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    """BookViewSet."""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    search_fields = ['title']

    def get_queryset(self):
        if self.request.query_params.get('term'):
            self.queryset = book_service.get_by_term(self.request.query_params.get('term'))
        return self.queryset