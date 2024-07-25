from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='author-list'),
    path('authors/', views.AuthorView.as_view()),
    path('authors/<int:pk>', views.AuthorInstanceView.as_view(), name='author-instance'),
]