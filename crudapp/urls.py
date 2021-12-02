from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('blog/', views.blog,name='blog'),
    path('home/', views.home,name='home'),
    path('create/', views.createitem,name='createitem'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login')
]