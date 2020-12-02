"""Book service module."""
from wisatabook.models import Book

class BookService:
    """Book Service Class."""

    def get_by_term(self, term):
        """Get book by term."""
        books = Book.objects.filter(title__icontains=term)[:10]
   
        return books

book_service = BookService()