import uuid
from django.db import models

# Create your models here.
class Book(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title  = models.CharField(max_length = 500)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    description = models.TextField(default=None)
    price = models.FloatField()
    image_url = models.ImageField(upload_to = 'books', blank = True, null = True)
    book_available = models.BooleanField(default=False)
    publication_date = models.DateField()
    language = models.CharField(max_length = 100, null=True, blank=True)
    pages = models.IntegerField(default=0)

    def __str__(self):
        return f'Book: {self.title}'


class Author(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length = 250)

    def __str__(self):
        return self.name