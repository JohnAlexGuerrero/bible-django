from django.db import models
from django.urls import reverse

from Reference.models import Verse

# Create your models here.
class Epoch(models.Model):
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
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Events")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Event_detail", kwargs={"pk": self.pk})

class ReferenceEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("ReferenceEvent")
        verbose_name_plural = ("ReferenceEvents")

    def __str__(self):
        return self.event.title

    def get_absolute_url(self):
        return reverse("ReferenceEvent_detail", kwargs={"pk": self.pk})
