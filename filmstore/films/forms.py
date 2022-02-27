from django.forms import ModelForm, CheckboxSelectMultiple, Form, FileField

from .models import Director, Movie, Genre


class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = "__all__"
        exclude = ["id"]


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        exclude = ["id"]
        widgets = {
            'genres': CheckboxSelectMultiple()
        }


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"
        exclude = ["id"]


class DocumentForm(Form):
    docfile = FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
