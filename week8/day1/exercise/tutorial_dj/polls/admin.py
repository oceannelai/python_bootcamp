from django.contrib import admin
from .models import Person, ImageProfile, Post, Category, Email, Address #import the Person model

# Register your models here.
admin.site.register(Person)
admin.site.register(ImageProfile)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Email)
admin.site.register(Address)


