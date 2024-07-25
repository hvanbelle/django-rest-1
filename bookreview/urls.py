from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index_view, name='author-book-list'),
    path('authors/', views.AuthorView.as_view()),
    path('authors/<int:pk>', views.AuthorInstanceView.as_view(), name='author-instance'),
    path('books/', views.BookView.as_view()),
    path('books/<int:pk>', views.BookInstanceView.as_view(), name='book-instance'),
]