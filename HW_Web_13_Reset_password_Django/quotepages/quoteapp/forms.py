from django.db.models import ForeignKey, CASCADE
from django.forms import ModelForm, CharField, TextInput, DateField, ModelChoiceField, Select, ChoiceField
from .models import Tag, Quote, Author


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=100, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    born_date = DateField(required=True)
    born_location = CharField(min_length=3, max_length=100, required=True, widget=TextInput())
    bio = CharField(min_length=3, max_length=1000, required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'bio']


class QuoteForm(ModelForm):
    quote = CharField(min_length=5, max_length=1000, required=True, widget=TextInput())
    # author = Author.objects.values()[0]
    author = "pass"

    class Meta:
        model = Quote
        fields = ['quote', 'author']
        exclude = ['tags']