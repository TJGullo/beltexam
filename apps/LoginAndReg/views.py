from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.urls import reverse
from .models import User
# from .models import Email
# Create your views here.

def index(request):
    context = {
    'new_user': User.objects.all()
    }
    return render(request, 'LoginAndReg/index.html', context)

def register(request):
    if request.method == 'POST':
        print 'in process method'
        print request.POST

        response = User.objects.validate_new_user(request.POST)

        if response[0] == False:
            for error in response[1]:
                messages.error(request, error)
                print 'response[0] was False'
                print error
            return redirect('users:index')
        else:
            print '9'*50
            print 'got to the "else"'
            print response[1]
            try:
                request.session['first_name'] = response[1].first_name
                request.session['id'] = int(response[1].id)
            except MultiValueDictKeyError:
                print "could not save to session!!!!"
            return redirect('users:success')
    else:
        return redirect('users:index')

def login(request):
    if request.method == 'POST':
        response = User.objects.validate_login(request.POST)
        if response[0] == False:
            for error in response[1]:
                messages.error(request, error)
            return redirect('users:index')
        else:
            request.session['first_name'] = response[1].first_name
            request.session['id'] = int(response[1].id)
            print request.session['id'], "This is the session ID"
            return redirect('users:success')

    return redirect('users:index')





def success(request):
        print "*"*50
        return render(request, 'LoginAndReg/success.html')


def logout(request):
    return redirect('users:index')
