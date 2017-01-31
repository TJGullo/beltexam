from __future__ import unicode_literals
from ..LoginAndReg.models import User
from django.db import models

# Create your models here.
class WishesManager(models.Manager):
    def fetch_items(self):
        items = self.all().order_by("-created_at")[:5]
        return items

    def create_item(self, data):
        print data
        errors = []
        item = data['item']
        if Wishes.objects.filter(item=item):
            errors.append('Item already exists. Please enter a different item')

        if len(item) < 3:
            errors.append('Item must be atleast 3 characters long')

        if errors:
            print "*"*50
            print errors
            return [False, errors]
        else:
            print "1"*50
            try:
                item = self.create(item=item)
                print item
            except NameError:
                pass
            return [True, item]


class Wishes(models.Model):
    user = models.ForeignKey('LoginAndReg.User')
    item = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishesManager()
