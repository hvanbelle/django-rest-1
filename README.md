# django-rest-1

## Links
- https://code.tutsplus.com/beginners-guide-to-the-django-rest-framework--cms-19786t

## Commands 1
- pip install django
- pip install djangorestframework
- pip install python-dotenv
- django-admin startproject core .
- python manage.py startapp bookreview
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser

## Commands 2 
- python manage.py shell
- from bookreview.models import Book,Author
- author = Author.objects.get(pk=1)
- author.id
- author.first_name
- author.last_name
- authors=Author.objects.all()
- authors
- from bookreview.serializers import AuthorSerializer
- author = Author.objects.get(pk=1)
- serialized = AuthorSerializer(author)
- serialized.data