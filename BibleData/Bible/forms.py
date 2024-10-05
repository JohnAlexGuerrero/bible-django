from django import forms

from Bible.models import Book

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ("title","description","title_short","author","category")
