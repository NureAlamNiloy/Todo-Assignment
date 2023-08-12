from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = "homePage"),
    path('addTask/',views.addTask, name = "addTask"),
    path('showTask/',views.showTask, name = "showTask"),
    path('EditTask/<int:id>',views.editTask, name = "EditTask"),
    path('DeleteTask/<int:id>',views.deleteTask, name = "DeleteTask"),
    path('completeTask/<int:id>',views.completeTask, name = "completeTask"),
    path('completeTasks/', views.completeTasks, name='completeTasks'),
]