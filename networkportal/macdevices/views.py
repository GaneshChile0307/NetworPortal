# from django.shortcuts import render
# from devices.models import Device

# def device_list(request):
#     devices = Device.objects.all()
#     return render(request, 'devices/device_list.html', {'devices': devices})

from .models import Device
from django.http import HttpResponse
from django.shortcuts import render

# def device_list(request):
#     new_record = Device(name='test', mac_address='10:48:48:df48')
#     new_record.save()
#     return HttpResponse(f'Device saved successfully!')

def device_list(request):
    devices = Device.objects.all()
    return render(request, 'devices/device_list.html', {'devices': devices})