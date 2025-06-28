from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand


categories = ['Sports', 'Technologies', 'Science', 'Art', 'Food']



class Command(BaseCommand):
    help = "This command insert category data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing Data
        Category.objects.all().delete()


        categories = ['Sports', 'Technologies', 'Science', 'Art', 'Food']

        for category_name in categories:
            Category.objects.create(name = category_name)  

        self.stdout.write(self.style.SUCCESS("Completed Inserting Data!"))     
        


