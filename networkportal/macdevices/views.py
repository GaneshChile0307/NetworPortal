
import re
from .forms import AddDeviceForm
from django.http import JsonResponse
from .models import Device
from django.shortcuts import render
from django.conf import settings
from django.views import View
from rest_framework.views import APIView


class DeviceList(APIView):
    def get(self, request):
        devices = Device.objects.all()
        context = {'devices': devices , 'api_key': settings.API_KEY}
        return render(request,'macdevices/device-list.html',context) 

class AddDevice(APIView):
    def post(self, request):
        form = AddDeviceForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mac_address = form.cleaned_data['mac_address']
            if not re.match('^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac_address):
                return JsonResponse({'success': False, 'message': 'Invalid MAC address format'})
            device = Device(name=name, mac_address=mac_address)
            device.save()
            return JsonResponse({'message': 'Device added successfully.'})
        else:
            return JsonResponse({'message': 'Invalid form data.'}, status=400)  
        
    def get(self, request):
        form = AddDeviceForm()
        return render(request, 'macdevices/add_device.html', {'form': form})
