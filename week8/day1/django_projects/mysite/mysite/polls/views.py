from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def about (request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profile_user(request):

    context = {
        'first_name': 'Oceanne',
        'last_name': 'lai',
        'gender': 'female'
    }
    return render(request,'profile_user.html',context)
