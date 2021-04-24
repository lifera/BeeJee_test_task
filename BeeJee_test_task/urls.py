from django.urls import path, include
from task_app.views import TaskListView, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('create/', TaskCreate.as_view(), name='task_create'),
    path('edit/<int:pk>', TaskUpdate.as_view(), name='task_update'),
    path('delete/<int:pk>', TaskDelete.as_view(), name='task_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TaskListView.as_view(), name='tasks'),
]
