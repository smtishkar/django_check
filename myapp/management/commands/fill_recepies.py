from typing import Any
from django.core.management.base import BaseCommand
from myapp.models import Recipe, Category, User
from random import randint


# class Command(BaseCommand):
#     help = 'Create a new recipe'

#     user = User.objects.getall()
#     category = Category.objects.get

#     def handle(self, *args: Any, **options: Any) -> str | None:
#         for i in range(1,11):
#             recipe = Recipe(
#                 title = f'title{i}'
#                 description = f'description of the recipe {i}'
#                 steps = f'Steps description'
#                 cooking_time = randint(0,50), randint(0,60)
#                 author
#                 categoty 
#             )