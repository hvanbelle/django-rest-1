from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView

# Create your views here.

# read-only mode
#class AuthorView(ListAPIView):
# read-write mode
class AuthorView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorInstanceView(generics.RetrieveAPIView):
    """
Returns a single author.
Also allows updating and deleting
"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

def index_view(request):
    """
Ensure the user can only see their own profiles.
"""
    response = {
        'authors': Author.objects.all(),
        # 'books': Book.objects.all(),
    }
    return render(request, 'index.html', response)