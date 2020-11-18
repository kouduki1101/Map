from django.contrib import admin
from django.urls import path
from django.db import models
from .views import maplist, maplist_detail
from . import views

urlpatterns = [

    path('list', views.list, name='list'),
    path('post/list', views.post_list, name='post_list'),
    path('detail/<int:pk>/', maplist_detail.as_view()),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/11/11', views.assistance_dog, name='assistance_dog'),
    path('post/2/2', views.online_diagnosis, name='online_diagnosis'),
    path('post/3/3', views.blood_donation, name='blood_donation'),
    path('post/4/4', views.book_online, name='book_online'),
    path('post/5/5', views.children_cafeteria, name='children_cafeteria'),
    path('post/6/6', views.female_doctor, name='female_doctor'),
    path('post/7/7', views.nursing_home, name='nursing_home'),
    path('post/8/8', views.resting_place, name='resting_place'),
    path('post/9/9', views.library, name='library'),
    path('post/10/10', views.sports_center, name='sports_center'),
    path('post/12/12', views.citizen_group, name='citizen_group'),
    path('post/13/13', views.univercity, name='univercity'),
    path('post/14/14', views.municipality, name='municipality'),
    path('post/15/15', views.company, name='company'),

]
