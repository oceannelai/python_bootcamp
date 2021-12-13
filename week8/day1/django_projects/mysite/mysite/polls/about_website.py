from django.urls import path #path function
from . import views # . is shorthand for the current directory

urlpatterns = [
    path('about_website/', views.about_website),

]