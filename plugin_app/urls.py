from django.urls import path, include
from plugin_app import views

app_name = 'plugin_app'
urlpatterns = [
    # path("", views.home, name='home'),
    path("", views.react_home, name='home'),
    path("install", views.install, name='install'),
    path("sidebar", views.sidebar, name='sidebar'),
]
