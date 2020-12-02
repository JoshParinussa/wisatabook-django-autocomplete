"""Book serializer module."""

from rest_framework import serializers

# from rest_flex_fields import FlexFieldsModelSerializer

from wisatabook.models import Book

# from api.serializers.asset import AssetSerializer

class BookSerializer(serializers.ModelSerializer):
    """BookSerializer."""

    class Meta:  # noqa D106
        model = Book
        fields = '__all__'