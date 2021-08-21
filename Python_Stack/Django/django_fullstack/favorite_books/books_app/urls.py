from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('books', views.books),
    path('add', views.add),
    path('books/<int:book_id>', views.book),
    path('books/<int:book_id>/update', views.update),
    path('books/<int:book_id>/delete', views.delete),
    path('books/<int:book_id>/favorite', views.favorite),
    path('logout', views.logout),

	]