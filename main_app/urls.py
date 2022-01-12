from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # 'comics/' - Comics Index Route
    path('comics/', views.comics_index, name='index'),
]