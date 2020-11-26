from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        return '{} - {}'.format(self.id, self.firstname + self.lastname)


class Book(models.Model):
    title = models.CharField(max_length=255)
    rating = models.CharField(max_length=10)
    author = models.ForeignKey(Author, related_name='book_set', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.id, self.title)
