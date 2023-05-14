
from django.urls import path
from . import views 


urlpatterns = [
    path('device_list/', views.DeviceList.as_view(), name='device_list'),
    path('add_device/', views.AddDevice.as_view(), name='add_device'),
    path('verify_api_key/', views.VerifyAPIKey.as_view(), name='verify_api_key'),

]
