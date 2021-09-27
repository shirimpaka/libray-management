from django.db import models
from authors.models import Author
# Create your models here.


class Book(models.Model):

    CATEGORIES = (
        ('Romantic', 'Romantic'),
        ('Adult', 'Adult'),
        ('Fiction', 'Fiction')
    )

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORIES, default='Romantic')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
