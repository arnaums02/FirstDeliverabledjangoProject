"""
URL configuration for FirstDeliverabledjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from films.views import BookListView, book_detail, create_book, create_review, actor_detail, create_actors, register_user

from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register_user, name='register'),  # Ruta para el registro de usuarios
    path('', BookListView.as_view(), name='book_list'),
    path('film/<int:pk>/', book_detail, name='book_detail'),
    path('film/create/', create_book, name='create_book'),
    path('film/<int:pk>/review/create/', create_review, name='review_create'),
    path('actor/<int:pk>/', actor_detail, name='actor_detail'),
    path('create/actors/', create_actors, name='create_actors'),


    # NOT RECOMMENDED! but can be used to serve static content if we are on DEBUG=False
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
