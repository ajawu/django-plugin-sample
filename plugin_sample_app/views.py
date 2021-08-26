from django.http import HttpResponse
from plugin_sample_app.forms import SampleForm


def hello(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
    return HttpResponse('Hello World')
