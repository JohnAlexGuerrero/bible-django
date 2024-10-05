from django.db import models
from django.urls import reverse

import uuid

# Create your models here.
class Thing(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = ("Thing")
        verbose_name_plural = ("Things")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Thing_detail", kwargs={"pk": self.pk})

class Commandment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    description = models.TextField()
    

    class Meta:
        verbose_name = ("Commandment")
        verbose_name_plural = ("Commandments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Commandment_detail", kwargs={"pk": self.pk})
