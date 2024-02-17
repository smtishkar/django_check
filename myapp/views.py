from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipe
from random import choice
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import logout
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


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})


def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'myapp/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                # messages.success(request,f'Hi, welcome back!')
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('/')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'myapp/login.html',{'form': form})
    

def logout_view(request):
    logout(request)
    return redirect('login')