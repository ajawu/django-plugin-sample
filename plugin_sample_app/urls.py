from django.urls import path
from plugin_sample_app import views

app_name = "plugin_sample_app"

urlpatterns = [
    path("tasks/", views.TaskListView.as_view()),
    path("tasks/<int:id>/", views.TaskDetailView.as_view()),
]
