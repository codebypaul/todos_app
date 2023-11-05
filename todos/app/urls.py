from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('',views.home_view, name='home view'),
    path('task-list/',TaskList.as_view(),name='task list'),
    path('task/<int:pk>',TaskDetail.as_view(),name='task'),
    path('task-create/',TaskCreate.as_view(),name='task create'),
    path('task-edit/<int:pk>',TaskUpdate.as_view(),name='task edit'),
    path('task-delete/<int:pk>',TaskDelete.as_view(),name='task delete'),

]