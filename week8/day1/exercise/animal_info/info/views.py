
from django.shortcuts import render
import json




def animal(request, id):
    with open('/Users/admin/Desktop/python_bootcamp/week8/day1/exercise/file.json') as f:
        data = json.load(f)
        animals = data['animals']
        for animal in animals:
            if int(id) == animal['id']:
                print(id, animal['id'])
                return render(request, 'animal.html', context={'animal': animal})
    return render(request, 'animal.html', context={'animal': {}})


def family(request, id):
    with open('/Users/admin/Desktop/python_bootcamp/week8/day1/exercise/file.json') as f:
        data = json.load(f)
        animals = data['animals']
        families = data['families']
        for family in families:
            if int(id) == family['id']:
                animals = [animal for animal in animals if animal['family'] == int(id)]
                print(animals)
                return render(request, 'family.html', context={'animals': animals, 'name': family['name']})
    return render(request, 'family.html', context={'families': []})