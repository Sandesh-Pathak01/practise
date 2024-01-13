from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('navprofile/Profilepage/<int:id>', views.profilepage, name='profile'),

    path('profile/<int:id>', views.profile, name='profileedit'),

    path('navprofile/', views.nav_profile, name='navprofile'),

    path('cmts/', views.add_comments, name='cmts'),
    path('posts/', views.add_posts, name='posts'),
    path('like/', views.likes, name='like'),
]