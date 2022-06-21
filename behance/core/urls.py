from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('singlework/<str:pk>/', views.singlework, name='singlework'),
    path('creatework/', views.creatework, name='creatework'),
]