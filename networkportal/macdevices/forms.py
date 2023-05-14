from django import forms
from django.core.validators import RegexValidator
from .models import Device

class AddDeviceForm(forms.Form):
    mac_address_validator = RegexValidator(
        regex=r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$',
        message='Invalid MAC address format'
    )

    name = forms.CharField(max_length=10, required=True)
    mac_address = forms.CharField(max_length=17, required=True,validators=[mac_address_validator])

    class Meta:
        model = Device
        fields = ['name', 'mac_address']