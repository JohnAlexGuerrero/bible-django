from django.db import models
from django.urls import reverse

# Create your models here.
        
class Book(models.Model):
    title = models.CharField(max_length=50, unique=True)
    chapters = models.IntegerField()
    author = models.ForeignKey("app.Model", on_delete=models.CASCADE)
    description = models.TextField()
    title_short = models.CharField(max_length=10, unique=True)
    
    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})
