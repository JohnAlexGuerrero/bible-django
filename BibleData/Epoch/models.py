from django.db import models
from django.urls import reverse

import uuid

# Create your models here.
class Epoch(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    period_year = models.FloatField()

    class Meta:
        verbose_name = ("Epoch")
        verbose_name_plural = ("Epochs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Epoch_detail", kwargs={"pk": self.pk})

class Event(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=150)
    description = models.TextField()
    epoch = models.ForeignKey(Epoch, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Events")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Event_detail", kwargs={"pk": self.pk})

