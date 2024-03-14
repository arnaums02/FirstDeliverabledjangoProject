from films.models import Film, Review
from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'author', 'genre', 'duration']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
