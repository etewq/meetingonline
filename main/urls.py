from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('profiles/', views.datinglist, name='datinglist'),
    path('profile/<int:pk>/', views.datingprofile, name='datingprofile'),
    path('chatlist/', views.chatlist, name='chatlist'),
    path('create/', views.profile_create, name='profile_create'),
    path('signup/', views.signup_page, name='signup_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_action, name='logout_action'),
    path('profile/update/<int:pk>/', views.profile_update, name='profile_update'),
]

