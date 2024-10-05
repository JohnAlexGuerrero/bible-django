from django.db import models
from django.urls import reverse

import uuid

from Bible.models import Book
from Person.models import Person
from Epoch.models import Event
from Place.models import Place
from Thing.models import Thing, Commandment

# Create your models here.
class Cita(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter = models.IntegerField()
    verse = models.IntegerField()

    class Meta:
        verbose_name = ("Cita")
        verbose_name_plural = ("Citas")

    def __str__(self):
        return self.get_cita_reference

    def get_absolute_url(self):
        return reverse("Cita_detail", kwargs={"pk": self.pk})
    
    def get_cita_reference(self):
        return f'{self.book.title_short}. {self.chapter}: {self.verse}'

class RelationshipCita(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True, default=None)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True, default=None)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True, blank=True, default=None)
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE, null=True, blank=True, default=None)
    commandment = models.ForeignKey(Commandment,on_delete=models.CASCADE, null=True, blank=True, default=None)

    class Meta:
        verbose_name = ("RelationshipCita")
        verbose_name_plural = ("RelationshipCitas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("RelationshipCita_detail", kwargs={"pk": self.pk})
