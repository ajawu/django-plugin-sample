from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    return render(request, template_name="plugin_app/index.html")


def react_home(request):
    return render(request, "index.html")


def install(request):
    data = {
        "name": "Sample Plugin",
        "description": "Simple proof of concept plugin in flask",
        "sidebar_url": "/sidebar",
        "install_url": "/install",
        "template_url": "/",
    }
    return JsonResponse(data, status=200)


def sidebar(request):
    data = {"icon": "Hello World", "text": "Channel name"}
    return JsonResponse(data, status=200)
