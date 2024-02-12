from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# ○ Название
# ○ Описание
# ○ Шаги приготовления
# ○ Время приготовления
# ○ Изображение
# ○ Автор
# ○ *другие поля на ваш выбор, например ингредиенты и т.п.


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f'Category_name: {self.name}'

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    steps = models.TextField()
    cooking_time = models.TimeField()
    img = models.ImageField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return f'Title: {self.title}, description: {self.description}, steps: {self.steps}, cooking_time: {self.cooking_time}, author: {self.author}, category: {self.category}'