from django.contrib import admin
from films.models import Film, Review, Actor


class LibroAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'duration')
    filter_horizontal = ('actors',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('film', 'user', 'content', 'rating')


class ActorAdmin(admin.ModelAdmin):
 list_display = ('name', 'age', 'country')


# Register your models here.
admin.site.register(Film, LibroAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Actor, ActorAdmin)
