from django.urls import reverse
from django.db import models

testaments = (
    ('AT', 'antiguo testamento'),
    ('NT', 'nuevo testamento'),
)

class Collection(models.Model):
    name = models.CharField(("nombre"), max_length=50, unique=True)
    section = models.CharField(("seccion"), max_length=50, choices=testaments)
    summary = models.TextField(("descripcion"))

    class Meta:
        verbose_name = ("Collections")
        verbose_name_plural = ("Collections")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Collections_detail", kwargs={"pk": self.pk})


class Book(models.Model):
    name = models.CharField(("nombre"), max_length=50, unique=True)
    chapters = models.IntegerField(("capitulos"))
    summary = models.TextField(("resumen"))
    collection = models.ForeignKey(Collection, verbose_name=("collections"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})

class History(models.Model):
    title = models.CharField(("titulo"), max_length=50, unique=True)

    class Meta:
        verbose_name = ("History")
        verbose_name_plural = ("Histories")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("History_detail", kwargs={"pk": self.pk})

class Text(models.Model):
    book = models.ForeignKey(Book, verbose_name=("books"), on_delete=models.CASCADE)
    chapter = models.IntegerField(("capitulo"))
    history = models.ForeignKey(History, verbose_name=("histories"), on_delete=models.CASCADE)
    verse = models.IntegerField(("verso"))
    description = models.TextField(("texto"))

    class Meta:
        verbose_name = ("Text")
        verbose_name_plural = ("Texts")

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("Text_detail", kwargs={"pk": self.pk})

class Quotes(models.Model):
    name = models.CharField(("cita"), max_length=25)
    text = models.ForeignKey(Text, verbose_name=("texts"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Quotes")
        verbose_name_plural = ("Quotes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Quotes_detail", kwargs={"pk": self.pk})


class Links(models.Model):
    text = models.ForeignKey(Text, verbose_name=("texts"), on_delete=models.CASCADE)
    quote = models.ManyToManyField(Quotes, verbose_name=("quotes"))

    class Meta:
        verbose_name = ("Link")
        verbose_name_plural = ("Links")

    def __str__(self):
        return f'{self.text} - {self.quote}'

    def get_absolute_url(self):
        return reverse("Links_detail", kwargs={"pk": self.pk})

class Character(models.Model):
    name = models.CharField(("nombre"), max_length=50, unique=True)

    class Meta:
        verbose_name = ("Character")
        verbose_name_plural = ("Characters")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Character_detail", kwargs={"pk": self.pk})

class CharacterStorie(models.Model):
    character = models.ForeignKey(Character, verbose_name=("characters"), on_delete=models.CASCADE)
    stories = models.ManyToManyField(History, verbose_name=("histories"))

    class Meta:
        verbose_name = ("CharacterStorie")
        verbose_name_plural = ("CharacterStories")

    def __str__(self):
        return self.character.name

    def get_absolute_url(self):
        return reverse("CharacterStorie_detail", kwargs={"pk": self.pk})
