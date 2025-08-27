from django.urls import path, include
from .views import (
    index,
    TaskListView,
    TagListView,
    TaskDetailView,
    TagDetailView,
    TaskCreateView,
    TagCreateView,
    TaskUpdateView,
    TagUpdateView,
    TaskDeleteView,
    TagDeleteView
)


app_name = 'tasks'


task_patterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit'),
    path('<int:pk>/add/', TaskCreateView.as_view(), name='task-add'),
]


tag_patterns = [
    path('', TagListView.as_view(), name='tag-list'),
    path('<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
    path('<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
    path('<int:pk>/edit/', TagUpdateView.as_view(), name='tag-edit'),
    path('<int:pk>/add/', TagCreateView.as_view(), name='tag-add'),
]

urlpatterns = [
    path('', index, name='index'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('tasks/', include(task_patterns)),
    path('tags/', include(tag_patterns)),
]


