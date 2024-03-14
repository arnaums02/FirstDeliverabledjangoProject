from django.contrib import admin
from films.models import Film, Review


class LibroAdmin(admin.ModelAdmin):
 list_display = ('title', 'author', 'genre', 'duration')


class ReviewAdmin(admin.ModelAdmin):
 list_display = ('film', 'user', 'content', 'rating')


# Register your models here.
admin.site.register(Film, LibroAdmin)
admin.site.register(Review, ReviewAdmin)