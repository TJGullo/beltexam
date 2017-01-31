from django.conf.urls import url
from . import views

app_name = 'LoginAndReg'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^success$', views.success, name='success'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^login$', views.login, name='login'),
    url(r'^', views.index),
]