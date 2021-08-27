from django.urls import path
from todo import views

app_name = "plugin_sample_app"

urlpatterns = [
    path("tasks/", views.TaskListView.as_view()),
    path("tasks/<int:id>/", views.TaskDetailView.as_view()),
]
