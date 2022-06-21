from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('otherprofile/<str:pk>/', views.other_profile, name='other_profile'),
    path('', views.userAccount, name='profile'),
]