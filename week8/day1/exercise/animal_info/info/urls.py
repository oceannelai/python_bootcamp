from django.urls import path
from . import views

# one urlpattern per line
urlpatterns = [
    path('animal/<int:id>', views.animal),
    path('family/<int:id>', views.family),
]