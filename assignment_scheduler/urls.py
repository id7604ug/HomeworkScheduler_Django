from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='main_menu'),
    url(r'^assignment_list/$', views.assignment_list, name='assignment_list'),
    url(r'^assignment/new/$', views.add_assignment, name='add_assignment'),
    # url(r'^$', views.view_all_assignments, name='view_all_assignments'),
    # url(r'^delete_assignment/$', views.delete_assignment, name='delete_assignment'),
    url(r'^assignment/(?P<id>\d+)/$', views.assignment_read, name='assignment_read'),
    url(r'^delete_assignment/(?P<id>\d+)/$', views.assignment_delete, name='assignment_delete'),
    url(r'^check_due_assignments/$', views.check_due_assignments, name='check_due_assignments')

]
