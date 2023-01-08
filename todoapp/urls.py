from django.urls import path,include

from todoapp import views

urlpatterns = [
path('',views.Index,name="Index"),
path('home',views.home,name="home"),
path('register',views.register,name="register"),
path('login',views.login,name="login"),
path('logout',views.logout,name="logout"),
path('delete/<int:taskid>',views.delete,name="delete"),
path('edit/<int:taskid>',views.edit,name="edit"),
path('TaskListView/',views.TaskListView.as_view(),name="TaskListView"),
path('TaskDetailView/<int:pk>',views.TaskDetailView.as_view(),name="TaskDetailView"),
path('TaskUpdateView/<int:pk>',views.TaskUpdateView.as_view(),name="TaskUpdateView"),
path('TaskDeleteView/<int:pk>',views.TaskDeleteView.as_view(),name="TaskDeleteView"),
path('sample',views.sample,name="sample"),
path('sample2',views.sample2,name="sample2")


    
]