from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.urls import reverse
from .models import Wishes
from ..LoginAndReg.models import User
# Create your views here.

def index(request):
    print request.session.keys()
    items = Wishes.objects.all()

    context = {
        'items': items,
    }
    return render(request, 'wish_list/index.html', context)

def new(request):
    context = {
        'items': Wishes.objects.all()
    }
    return render(request, 'wish_list/new.html', context)


def create(request):

    response = Wishes.objects.create_item(request.POST)
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
