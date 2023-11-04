from django.urls import path
from . import views
from .views import TaskList, TaskDetail

urlpatterns = [
    path('',views.home_view, name='home view'),
    path('task-list/',TaskList.as_view()),
    path('task-list/<int:pk>',TaskDetail.as_view())

]