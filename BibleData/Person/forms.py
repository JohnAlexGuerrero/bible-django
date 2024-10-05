from django import forms

from Person.models import Person

class PersonForm(forms.ModelForm):
    
    class Meta:
        model = Person
        fields = ("name","surname","age","sex","attribute_name","country","tribe")
