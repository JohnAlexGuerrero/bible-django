from django.db import models
from django.urls import reverse

from Reference.models import Verse

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50, unique=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices=['Male','Female'], null=True, blank=True)
    attribute_name = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=100)
    tribe = models.CharField(max_length=100, null=True, blank=True)
    days_of_lived = models.IntegerField(blank=True, null=True)


    class Meta:
        verbose_name = ("Person")
        verbose_name_plural = ("Persons")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("King_detail", kwargs={"pk": self.pk})

class ReferencePerson(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("ReferencePerson")
        verbose_name_plural = ("ReferencePersons")

    def __str__(self):
        return self.person

    def get_absolute_url(self):
        return reverse("ReferencePerson_detail", kwargs={"pk": self.pk})

