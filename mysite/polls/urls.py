from django.contrib import admin
from django.urls import path, include
from polls import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.contact, name='contact'),
]

