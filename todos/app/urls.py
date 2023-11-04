from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate

urlpatterns = [
    path('',views.home_view, name='home view'),
    path('task-list/',TaskList.as_view(),name='task list'),
    path('task/<int:pk>',TaskDetail.as_view(),name='task'),
    path('task-create/',TaskCreate.as_view(),name='task create')

]