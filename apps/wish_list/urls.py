from django.conf.urls import url
from . import views

app_name = 'wish_list'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^create/$', views.create, name='create'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
    url(r'^add/(?P<wish_id>\d+)$', views.add, name='add'),
    url(r'^remove/(?P<wish_id>\d+)$', views.remove, name='remove'),
    url(r'^(?P<wish_id>\d+)/$', views.show, name='show'),
    # url(r'^users/(?P<id>\d+)/$', show_user, name='show_user'),
]
