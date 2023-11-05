from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.home_view, name='home view'),
    # Auth views
    path('sign-up/',CustomLoginView.as_view(), name='sign-up'),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='home view'), name='logout'),
    path('profile/',views.profile, name='profile'),
    # App views
    path('task-list/',TaskList.as_view(),name='task list'),
    path('task/<int:pk>',TaskDetail.as_view(),name='task'),
    path('task-create/',TaskCreate.as_view(),name='task create'),
    path('task-edit/<int:pk>',TaskUpdate.as_view(),name='task edit'),
    path('task-delete/<int:pk>',TaskDelete.as_view(),name='task delete'),

]