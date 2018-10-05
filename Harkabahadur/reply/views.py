from django.shortcuts import render
from django.http import HttpResponse

from .models import response


def index(request):
    if request.method == 'GET':
        sensor_value = request.GET.get('sensor_value')
        if sensor_value is not None:
            # return HttpResponse('You sent a value: ' + sensor_value)
            return render(request, 'index.html', {'name': 'milan'})
    return HttpResponse('You are at the reply homepage')
