from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.index, name= 'index'),
    path('all_emp', views.all_emp, name= 'all_emp'),
    path('add_emp', views.add_emp, name= 'add_emp'),
    path('remove_emp', views.remove_emp, name= 'remove_emp'),
    path('remove_emp/<int:emp_id>', views.remove_emp, name= 'remove_emp'),
    path('fillter_emp', views.fillter_emp, name= 'fillter_emp'),
]