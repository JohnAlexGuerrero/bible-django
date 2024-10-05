from django.db import models
from django.db.models import Sum, Count
from django.urls import reverse

from Person.models import Person

import uuid

# Create your models here.
        
class Book(models.Model):
    class Category(models.TextChoices):
        LA_LEY = 'la ley'
        HISTORICOS = 'historicos'
        POETICOS_Y_DE_SABIDURIA = 'poeticos y de sabiduria'
        PROFETAS_MAYORES = 'profetas mayores'
        PROFETAS_MENORES = 'profetas menores'
        EVAGENLICOS = 'evangelicos'
        CARTAS_PAULINAS = 'cartas paulinas'
        CARTAS_GENERALES = 'cartas generales'
        HISTORICOS_APOSTOLICOS = 'historicos apostolicos'
        PROFETICOS = 'profeticos'
        
    title = models.CharField(max_length=50, unique=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    description = models.TextField()
    title_short = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    category = models.CharField(max_length=50, choices=Category.choices)
    
    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")
        ordering = ('created_at',)

    def __str__(self):
        return self.title.upper()

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})
    
