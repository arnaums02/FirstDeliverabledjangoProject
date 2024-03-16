from django.db.models import Avg
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from films.forms import BookForm, ReviewForm
from django.views.generic import ListView
from films.models import Film, Review, Actor


class BookListView(ListView):
    model = Film
    template_name = 'film_list.html'
    context_object_name = 'books'


def book_detail(request, pk):
    book = get_object_or_404(Film, pk=pk)
    return render(request, 'detail_film.html', {'book': book})


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk) # Redirigir al usuario a detalles del libro
    else:
        form = BookForm()
        return render(request, 'create_film.html', {'form': form})


def create_review(request, pk):
    book = get_object_or_404(Film, id=pk)
    # lo mismo que book = Libro.objects.get(id=pk) pero con control de fallos si no lo encuentra.
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.film = book
            review.user = request.user
            review.save()
            return redirect('book_detail', pk=book.id)
    else:
        form = ReviewForm()
        return render(request, 'create_review.html', {'form': form, 'book': book})


def actor_detail(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    return render(request, 'actor_detail.html', {'actor': actor})
