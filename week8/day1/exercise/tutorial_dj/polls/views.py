from django.shortcuts import render
from .models import Person, Post, Email, Address # import the models from polls/models.py

                    # get the first object because Person.objects.filter returns a QuerSet (ie. a list)


def index(request, name):

    person = Person.objects.get(first_name = name)

    context = {
        'page_title' : "Homepage",
        'user' : person
    }
    return render(request, 'homepage.html', context)

def posts(request, name, last_name):
    context = {
        'page_title' : "Posts",
        'posts' : Post.objects.filter(
            author__first_name=name),
        'email' : Email.objects.get().email,
        'address' : Address.objects.get().address

    }
    return render(request, 'posts.html', context)



