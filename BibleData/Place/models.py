from django.db import models
from django.urls import reverse

import uuid

# Create your models here.
class Place(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=150, unique=True)
    country = models.CharField(max_length=150)

    class Meta:
        verbose_name = ("Place")
        verbose_name_plural = ("Places")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Place_detail", kwargs={"pk": self.pk})
