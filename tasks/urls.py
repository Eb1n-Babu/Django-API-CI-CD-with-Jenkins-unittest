from django.urls import path
from .views import Tasks

urlpatterns = [
    path('tasks/', Tasks.as_view({'get':'list'}), name='task-list-create'),
    path('tasks/<int:pk>/', Tasks.as_view({'get':'list'}), name='task-detail'),
]