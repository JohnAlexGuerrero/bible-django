from django.shortcuts import render
from django.urls import reverse_lazy

from Bible.models import Book
from Bible.forms import BookForm

from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic import UpdateView

# Create your views here.

#view update book inf
class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "book/create.html"
    success_url = reverse_lazy('book_home')

#view main books
class BookHomeView(TemplateView):
    template_name = "book/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Book.objects.all()
        return context
    


#view list books
class BookListView(ListView):
    model = Book
    template_name = "book/list.html"


#view create one book
class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "book/create.html"
    success_url = reverse_lazy('book_list')