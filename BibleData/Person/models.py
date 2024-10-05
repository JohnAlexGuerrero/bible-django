from django.db import models
from django.urls import reverse
import uuid

class Characteristic(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=150, unique=True)
        
    class Meta:
        verbose_name = ("Characteristic")
        verbose_name_plural = ("Characteristics")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Characteristics_detail", kwargs={"pk": self.pk})

# Create your models here.
class Person(models.Model):
    class Gender(models.TextChoices):
        MASCULINO = 'Masculino'
        FEMENINO = 'Femenino'
        
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=10, choices=Gender.choices)
    attribute_name = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    tribe = models.CharField(max_length=100, null=True, blank=True)
    characters = models.ManyToManyField(Characteristic, blank=True, null=True)

    class Meta:
        verbose_name = ("Person")
        verbose_name_plural = ("Persons")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("King_detail", kwargs={"pk": self.pk})
    
    def get_day_of_lived(self)-> str:
        return f'{self.age * 365:,.0f} days'

class Relationship(models.Model):
    class Type(models.TextChoices):
        PADRE = 'Padre'
        MADRE = 'Madre'
        HIJO = 'Hijo'
        
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=50, choices=Type.choices)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Relationship")
        verbose_name_plural = ("Relationships")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Relationship_detail", kwargs={"pk": self.pk})

class RelationshipPerson(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    relationship = models.ForeignKey(Relationship, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("RelationshipPerson")
        verbose_name_plural = ("RelationshipPersons")

    def __str__(self):
        return f'{self.from_person} -> {self.to_person}'

    def get_absolute_url(self):
        return reverse("RelationshipPerson_detail", kwargs={"pk": self.pk})
