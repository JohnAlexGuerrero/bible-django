from django.db import models
from django.urls import reverse

from Bible.models import Book

# Create your models here.
class Verse(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter = models.IntegerField()
    verse = models.IntegerField()

    class Meta:
        verbose_name = ("Verse")
        verbose_name_plural = ("Verses")

    def __str__(self):
        return f'{self.book.title_short} {self.chapter} {self.verse}'

    def get_absolute_url(self):
        return reverse("Verse_detail", kwargs={"pk": self.pk})
