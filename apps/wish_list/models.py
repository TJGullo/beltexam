from __future__ import unicode_literals
from ..LoginAndReg.models import User
from django.db import models

# Create your models here.
class WishesManager(models.Manager):
    def fetch_items(self):
        items = self.all().order_by("-created_at")[:5]
        return items

    def create_item(self, data, user_id):
        print data
        errors = []
        item = data['item']
        if self.filter(item=item):
            errors.append('Item already exists. Please enter a different item')

        if len(item) < 3:
            errors.append('Item must be atleast 3 characters long')
        else:
            print data
            # self.create(item=data['item'])


        if errors:
            print "*"*50
            print errors
            return [False, errors]
        else:
            print "1"*50
            try:
                print item
                our_user = User.objects.get(id=user_id)
                print our_user.first_name
                item = Wishes.objects.create(item=item, created_by=our_user)
                # our_user.user_item.add(item)
                item.added_by.add(our_user)
            except NameError:
                pass
        return [True, item]

    def add_item(self, wish_id, user_id):
        print user_id, 'got this id from views in models now'
        our_user = User.objects.get(id=user_id)
        wish = Wishes.objects.get(id=wish_id)
        wish.added_by.add(our_user)
        print wish.item




class Wishes(models.Model):
    created_by = models.ForeignKey(User, related_name='created_item')
    added_by = models.ManyToManyField(User, related_name='user_item')
    item = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishesManager()
