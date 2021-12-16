import gmail as gmail
from django.db import models #import the models package. This line is already existing as soon as we use 'startapp'
from datetime import datetime
#Must inherit from Django Model class
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    has_pet = models.BooleanField(default=True)
    number_pet = models.IntegerField()

    def __str__(self):
    	return self.first_name

# THE POST IS the CHILD table 
# THE PERSON is the PARENT table

class ImageProfile (models.Model):
	# person field is primary key + foreign key
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    image = models.URLField()

    def __str__(self):
        return f'ImageProfile of {self.person}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(max_length=50)
    released_date = models.DateField(default = datetime.now())
    # ONE - TO - MANY = foreign key in childs table
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    # If you delete a person, his posts will be also deleted

    def __str__(self):
        return f'{self.title}'



class Category(models.Model):
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post, related_name='categories', blank=True)
# related_name is to retrieve the categories from a post
# Allows witing Post.categories -> QuerySet of all the Categories associated with the Post
    def __str__(self):
        return f'Category {self.name}'
class Email(models.Model):

    person = models.OneToOneField(
            Person,
            on_delete=models.CASCADE,
            primary_key=True,
        )
    email = models.CharField(max_length=200, unique=True, default='a @ gmail.com')

    def _str_(self):
        return f'Email {self.email}'

class Address(models.Model):
    person = models.ManyToManyField(Person)
    address = models.CharField(max_length=200)
    def __str__(self):
        return f'Address { self.address }'