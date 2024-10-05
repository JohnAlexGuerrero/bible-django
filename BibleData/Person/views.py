from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic import UpdateView

from Person.models import Person

from Person.forms import PersonForm



# Create your views here.
#view update person inf

#view home person
class PersonHomeView(TemplateView):
    template_name = "person/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Person.objects.all()
        return context
    

#view list person
class PersonListView(ListView):
    model = Person
    template_name = "person/list.html"

#view create person
class PersonCreateView(CreateView):
    model = Person
    template_name = "person/create.html"
    form_class = PersonForm
    success_url = reverse_lazy('person_list')