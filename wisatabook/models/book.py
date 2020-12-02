"""Book models."""
import uuid

from django.db import models


class Book(models.Model):
    """Book model."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, unique=True)
    short_summary = models.TextField()
    date_published = models.DateTimeField()

    def __str__(self):
        """String representation."""
        return self.title
