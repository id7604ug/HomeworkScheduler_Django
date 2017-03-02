from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='main_menu'),
    url(r'^$', views.assignment_list, name='assignment_list'),
    url(r'^assignment/new/$', views.add_assignment, name='add_assignment'),
]
