from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [   
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name = 'logout'),
    path('profile/', views.profile, name='profile'),
    path('',include('django.contrib.auth.urls')),
]