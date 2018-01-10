from django.contrib import admin
from django.urls import path

from articles import views

urlpatterns = [
    path('create/', views.articles_create, name="url1"),
    path('detail/<int:article_id>/', views.articles_detail, name="url2"),
    path('updat/', views.articles_update, name="url3"),
    path('list/', views.articles_list, name="url4"),
    path('delete/', views.articles_delete, name="url5"),
]