from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.urls import reverse
from .models import Wishes
from ..LoginAndReg.models import User
# Create your views here.

def index(request):
    print request.session.keys()
    our_items = Wishes.objects.filter(added_by__id=request.session['id'])
    print our_items, "*"*50
    other_items = Wishes.objects.exclude(added_by__id=request.session['id'])
    context = {
        'our_items': our_items,
        'other_items': other_items,
    }
    return render(request, 'wish_list/index.html', context)

def new(request):
    context = {
        'items': Wishes.objects.all()
    }
    return render(request, 'wish_list/new.html', context)


def create(request):
    user_id = request.session['id']
    response = Wishes.objects.create_item(request.POST, user_id)
    print "5"*50
    if response[0] == False:
        for error in response[1]:
            messages.error(request, error)
            print 'response[0] was False'
            print error
            return redirect('wishlist:new')
        else:
            print '9'*50
            print response[1]
            return redirect('wishlist:index')
    else:
        return redirect('wishlist:index')

def destroy(request, id):
    wish = Wishes.objects.get(id=id)
    wish.delete()
    return redirect('wishlist:index')

def add(request, wish_id):
    # adding item to own wish list
    u_id = request.session['id']
    print u_id, 'views user id'
    Wishes.objects.add_item(wish_id, u_id)
    return redirect('wishlist:index')

def remove(request, wish_id):
    # removing item from own wish list
    pass
