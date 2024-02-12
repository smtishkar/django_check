from typing import Any
from django.core.management.base import BaseCommand
from myapp.models import Category


class Command(BaseCommand):
    help = 'Create a new category'

    def handle(self, *args: Any, **options: Any) -> str | None:
        categories = ['пироги', 'салаты', 'основные_блюда', 'гарнир']
        for i in range(len(categories)):
            cateregory = Category(
                name = categories[i]
            )
            self.stdout.write(self.style.SUCCESS(f'Category {cateregory} created.'))
            cateregory.save()
