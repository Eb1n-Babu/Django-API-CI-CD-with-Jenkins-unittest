from django.urls import path
from .views import Tasks

urlpatterns = [
    path('tasks/', Tasks.as_view({'get':'list','post':'create'}), name='task-list-create'),
    path('tasks/<int:pk>/', Tasks.as_view({'get':'retrieve','put':'update','delete':'destroy'}), name='task-detail'),
]