from films.models import Film, Review, Actor
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Eliminar las restricciones de longitud de contraseña
        self.fields['password1'].widget.attrs.pop('min_length', None)
        self.fields['password1'].widget.attrs.pop('maxlength', None)
        self.fields['password1'].widget.attrs.pop('pattern', None)
        self.fields['password2'].widget.attrs.pop('min_length', None)
        self.fields['password2'].widget.attrs.pop('maxlength', None)
        self.fields['password2'].widget.attrs.pop('pattern', None)