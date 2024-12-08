from django.core.management.base import BaseCommand
from shop.models import Category, Item, Tag
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # print(Category.objects.all())
        
        expensive_items = Item.items.expensive_items()
        for item in expensive_items:
            print(item.name, item.price)
    