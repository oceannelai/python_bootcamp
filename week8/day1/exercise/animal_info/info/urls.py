

from django.urls import path
from . import views

# one urlpattern per line
urlpatterns = [
    path('family/<int:x>', views.family_list),
    path('animal/<int:x>', views.animal_stats),
    path('specific_family/<int:x>', views.family),
    path('/animals/', views.animals)
]