import datetime
import time

from django.shortcuts import render
from django.http import HttpResponse

from .models import response
from django import forms

# import requests


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


from django.views.decorators.csrf import csrf_exempt

import json

from . import models


@csrf_exempt
def test(request):
    if request.method == 'POST':
        for i in request.POST.lists():
            data = json.loads(i[0])
            break
        selectedButtonId = data['selectedButtonId']
        timeValue = data['timeValue']
        tolerance = data['tolerance']
        ts = time.time()
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime(
            '%Y-%m-%d %H:%M:%S')
        print(selectedButtonId, timeValue, tolerance, timeStamp)

        models.log(
            selectedButtonId=selectedButtonId,
            timeValue=timeValue,
            tolerance=tolerance,
            timeStamp=timeStamp).save()
        print('\n\n\nModel Saved...\n\n\n')
    return HttpResponse('Helo')
