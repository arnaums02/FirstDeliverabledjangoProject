from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True, null=True)
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor, related_name='films')

    def __str__(self):
        return self.title


class Review(models.Model):
     film = models.ForeignKey(Film, on_delete=models.CASCADE)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     content = models.TextField()
     rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])

     def __str__(self):
        return self.content


