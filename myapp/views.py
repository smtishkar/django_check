from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Recipe
from random import choice
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RecipeForm
from django.core.files.storage import FileSystemStorage
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


# def update_recipe(request, recipe_id):
#     recipe = get_object_or_404(Recipe, pk=recipe_id)
#     message = 'Ошибка данных'
#     if request.method == 'POST':
#         form = RecipeForm(request.POST, request.FILES)
#         if form.is_valid():

#             recipe.title = request.POST['title']
#             recipe.description = request.POST['description']
#             recipe.steps = request.POST['steps']
#             img = request.FILES["img"]
#             fs = FileSystemStorage()
#             fs.save(img.name, img)
#             recipe.img = img.name

#             recipe.category = request.POST['category']

#             recipe.save()
#             message = 'Рецепт изменен'
#     else:
#         form = RecipeForm()
#         message = 'Заполните форму создания рецепта'
#     context = {
#         "form": form,
#         "message": message
#     }
#     # return render(request, 'myapp/update_recepie.html', {'form': form, 'message': message})
#     return render(request, "myapp/update_recepie.html", context=context)


def update_recipe(request, recipe_id):
    message = 'Ошибка данных'
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = Recipe.objects.filter(pk=recipe_id).first()
            print(recipe.pk)
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            steps = form.cleaned_data['steps']
            cooking_time = form.cleaned_data['cooking_time']
            img = form.cleaned_data['img']
            fs = FileSystemStorage()
            recipe.img = img
            fs.save(img.name, img)
            category = form.cleaned_data['category']
            author = form.cleaned_data['author']
            recipe.title = title
            recipe.description = description
            recipe.steps = steps
            recipe.cooking_time = cooking_time
            recipe.category = category
            recipe.author = author
            # recipe = Recipe(title=title, description=description, steps=steps, cooking_time=cooking_time,
            #                  category=category, author=author, img=img)
            # recipe.save(update_fields=["title",'description', 'steps', 'cooking_time', 'category', 'author','img'])
            # recipe = Recipe.objects.filter(recipe_id).update(title=title, description=description, steps=steps, cooking_time=cooking_time,
            #                  category=category, author=author, img=img)
            # recipe.update(title=title)
            # recipe.save(update_fields=['title', 'description', 'steps', 'cooking_time', 'category', 'author','img'])
            recipe.save()
            # recipe.save(update_fields=["title"])
            print(recipe.pk, recipe.title)
            message = 'Рецепт изменен'
    else:
        form = RecipeForm()
        message = 'Заполните форму создания рецепта'
    return render(request, 'myapp/update_recepie.html', {'form': form, 'message': message})


def new_recipe(request):
    message = 'Ошибка данных'
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            # recipe = Recipe.objects.filter(pk=recipe_id).first()
            # print(recipe.pk)
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            steps = form.cleaned_data['steps']
            cooking_time = form.cleaned_data['cooking_time']
            img = form.cleaned_data['img']
            fs = FileSystemStorage()
            # recipe.img = img
            fs.save(img.name, img)
            category = form.cleaned_data['category']
            author = form.cleaned_data['author']
            # recipe.title = title
            # recipe.description = description
            # recipe.steps = steps
            # recipe.cooking_time = cooking_time
            # recipe.category = category
            # recipe.author = author
            recipe = Recipe(title=title, description=description, steps=steps, cooking_time=cooking_time,
                             category=category, author=author, img=img)
            # recipe.save(update_fields=["title",'description', 'steps', 'cooking_time', 'category', 'author','img'])
            # recipe = Recipe.objects.filter(recipe_id).update(title=title, description=description, steps=steps, cooking_time=cooking_time,
            #                  category=category, author=author, img=img)
            # recipe.update(title=title)
            # recipe.save(update_fields=['title', 'description', 'steps', 'cooking_time', 'category', 'author','img'])
            recipe.save()
            # recipe.save(update_fields=["title"])
            print(recipe.pk, recipe.title)
            message = 'Рецепт создан'
    else:
        form = RecipeForm()
        message = 'Заполните форму создания рецепта'
    return render(request, 'myapp/new_recipe.html', {'form': form, 'message': message})