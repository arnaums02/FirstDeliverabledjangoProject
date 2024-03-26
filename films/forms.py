from films.models import Film, Review, Actor
from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'author', 'genre', 'duration', 'actors']

    actors = forms.ModelMultipleChoiceField(queryset=Actor.objects.all(), widget=forms.SelectMultiple)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']



class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'age', 'country']
