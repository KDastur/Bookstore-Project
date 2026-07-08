from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    birth_date = models.DateField()
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    file = models.FileField(upload_to='ebooks/')
    stock = models.PositiveIntegerField(default=0)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title