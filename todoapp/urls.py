from django.urls import path,include

from todoapp import views
urlpatterns = [
path('',views.Index,name="Index"),
path('home',views.home,name="home"),
path('register',views.register,name="register"),
path('login',views.login,name="login"),
path('logout',views.logout,name="logout"),
path('delete/<int:taskid>',views.delete,name="delete"),
path('edit/<int:taskid>',views.edit,name="edit")


    
]