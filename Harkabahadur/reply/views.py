from django.shortcuts import render
from django.http import HttpResponse

from .models import response


def index(request):
    if request.method == 'GET':
        sensor_value = request.GET.get('sensor_value')
        if sensor_value is not None:
            # sensor = response.objects.get(pk=1)
            # on = response.objects.get(pk=2)
            # sensor.values=str(sens)
            # sensor.save()
            return HttpResponse('The data is $' + sensor_value + '#')
    return render(request, 'index.html')
    # return HttpResponse('You are at the reply homepage')
