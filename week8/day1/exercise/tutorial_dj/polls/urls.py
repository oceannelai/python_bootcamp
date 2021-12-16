from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('/index/<str:name>', views.index, name='index'),
    path('/name/<str:name>,<str:last_name>', views.posts, name='posts'),
]

# '' : empty string and /
# views.index : index function in views.py
# name='index' : name of the route