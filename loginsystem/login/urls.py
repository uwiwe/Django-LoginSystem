from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]