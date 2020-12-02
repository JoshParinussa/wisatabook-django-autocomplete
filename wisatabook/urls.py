from django.urls import path
from wisatabook.views.book import BookView

urlpatterns = [
    path('', BookView.as_view()),
]