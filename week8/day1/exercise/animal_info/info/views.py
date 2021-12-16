from django.shortcuts import render
import json
from .models import Family, Animals


# Create your views here.

# ./ - the location of the file we are working with

def family(request, x):
    # Model.objects.filter(id = x) returns the objects we are interested in
    family = Family.objects.filter(id=x).first()
    context = {"family": family}
    return render(request, 'family.html', context)


def family_list(request, x):
    filtered_animals = Animals.objects.filter(family_id = x)
    context = {"family": filtered_animals}
    return render(request, 'family.html', context)
def animal_stats(request, x):
    animal_x = Animals.objects.get(id = x)
    family_name = Family.objects.get(id = animal_x.family_id)
    context = {"family": family_name, "animal": animal_x}
    return render(request, 'animal.html', context)
def animals(request):

    animal_list = Animals.objects.all()
    return render(request, 'animals.html', {'animal_list':animal_list})
