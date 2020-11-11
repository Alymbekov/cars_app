from django.urls import path
from . import views
app_name = 'tasks'

urlpatterns = [
    #READ- RETRIEVE
    path('', views.TaskListView.as_view(), name='task_list'),
    #CREATE
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    #UPDATE
    path('<int:pk>/edit/', views.TaskEditView.as_view(), name='task_edit'),
    #DELETE
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),

]