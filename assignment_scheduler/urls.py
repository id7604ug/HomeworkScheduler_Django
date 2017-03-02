from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.assignment_list, name='assignment_list'),
]
