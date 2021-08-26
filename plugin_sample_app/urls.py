from django.urls import path
from plugin_sample_app import views

app_name = 'plugin_sample_app'

urlpatterns = [
    path('', views.hello, name='hello'),
]
