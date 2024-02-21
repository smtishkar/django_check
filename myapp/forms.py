from django import forms
from .models import Category, User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RecipeForm(forms.Form):
    title = forms.CharField(label='Название ,k.lf', max_length=100)
    description = forms.CharField(label='Описание')
    steps = forms.CharField(label='Шаги приготовления')
    cooking_time = forms.TimeField()
    author = forms.ModelChoiceField(label='выберите автора', queryset=User.objects.all())
    img = forms.ImageField(label='Изображение')
    category = forms.ModelChoiceField(label='Выберите категорию', queryset=Category.objects.all())