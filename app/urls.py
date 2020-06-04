from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('settings', views.settings),
    path('add_record', views.addRecord),
    path('delete_record', views.deleteRecord),
]
