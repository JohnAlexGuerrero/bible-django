from django.db import models
from django.urls import reverse

from Reference.models import Verse

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=150, unique=True)
    country = models.CharField(max_length=150)

    class Meta:
        verbose_name = ("Place")
        verbose_name_plural = ("Places")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Place_detail", kwargs={"pk": self.pk})

class PlaceReference(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Reference")
        verbose_name_plural = ("References")

    def __str__(self):
        return self.verse

    def get_absolute_url(self):
        return reverse("Reference_detail", kwargs={"pk": self.pk})
