from django.db import models

class BookStatus(models.TextChoices):
    TO_READ = 'TO_READ', 'Chcę przeczytać'
    READING = 'READING', 'Teraz czytam'
    READ = 'READ', 'Przeczytane'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=BookStatus.choices, default=BookStatus.TO_READ)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f'Review of {self.book.title} with rating {self.rating}'
