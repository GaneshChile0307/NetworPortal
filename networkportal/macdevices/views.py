
import re
from .forms import AddDeviceForm
from django.http import JsonResponse
from .models import Device
from django.shortcuts import render
from django.conf import settings
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
            # if not re.match('^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac_address):
            #     return JsonResponse({'success': False, 'message': 'Invalid MAC address format'})
            device = Device(name=name, mac_address=mac_address)
            device.save()
            return JsonResponse({'message': 'Device added successfully.'})
        else:
            if 'mac_address' in form.errors:
                return JsonResponse({'message': form.errors['mac_address'][0]}, status=400)
            else:
                return JsonResponse({'message': 'Invalid form data.'}, status=400)
        
    def get(self, request):
        form = AddDeviceForm()
        return render(request, 'macdevices/add_device.html', {'form': form})

class VerifyAPIKey(APIView):
    def get(self, request):
        api_key = request.GET.get('api_key')
        if api_key == settings.API_KEY:
            return Response({'is_valid': True}, status=status.HTTP_200_OK)
        else:
            return Response({'is_valid': False}, status=status.HTTP_401_UNAUTHORIZED)