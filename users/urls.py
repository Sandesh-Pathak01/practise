from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('Register-a-new-account/', views.signuppage, name='signup'),
    path('logout/', views.logoutt, name='logout'),
]