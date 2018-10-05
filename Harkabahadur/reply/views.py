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


@csrf_exempt
def test(request):
    if request.method == 'POST':
        # f = forms.Form(request.POST)
        # if f.is_valid():
        #     print(f.cleaned_data)
        print(dir(request.POST))
        print()
        for i in request.POST.lists():
            data = json.loads(i[0])
            break
        print(data['name'], data['age'])
        # print(a[0])
        # print('****', request.readlines())
    return HttpResponse('Helo')
