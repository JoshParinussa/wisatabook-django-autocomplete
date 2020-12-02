from django.conf import settings
from django.urls import include, path, re_path
from rest_framework import routers

from api.views import book as book_views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'book', book_views.BookViewSet)


urlpatterns = [
    path('v1/', include((router.urls, 'api_views'), )),
]
