from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('benefits/', views.benefits, name='benefits'),
      
]
