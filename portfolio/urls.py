from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='index'),
    path('project<int:pk>/', views.project, name='project'),
    path('posts/', views.posts, name='posts'),


    # AUTH

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
