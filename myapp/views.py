from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from random import choice
# Create your views here.



def index(request):
    recepies = Recipe.objects.all()
    random_recepies = []
    for _ in range(5):
        random_recepies.append(choice(recepies))
    print(random_recepies)
    context = {
        'random_recepies': random_recepies
    }
    return render(request, 'myapp/index.html', context=context)


def one_recepie(request, recepie_id: int):
    recepies = Recipe.objects.filter(pk=recepie_id).first()
    print(recepies)
    context ={
        'recepies': recepies
    }
    return render(request, 'myapp/one_recepie.html', context=context)