
from django.urls import path
from . import views 

urlpatterns = [
    path('devicelist/', views.DeviceList.as_view(), name='device_list'),
    path('add-device/', views.AddDevice.as_view(), name='add_device'),
]
