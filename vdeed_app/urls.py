from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('view_offerings', views.view_offerings, name='view_offerings'),    
]