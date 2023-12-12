from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('Profilepage/', views.profilepage, name='profile'),
    path('profile/', views.profile, name='profileedit'),
    path('cmts/', views.add_comments, name='cmts'),
    path('posts/', views.add_posts, name='posts'),
]