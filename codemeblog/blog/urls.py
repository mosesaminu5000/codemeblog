from django.urls import path

from . import views

urlspatterns =[
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
     path('<slug:slug>/', views.category, name='category_detail'),
]