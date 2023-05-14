from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home , name='blog-home'),
#     path('about/', views.about, name='blog-about'),
# ]

print("url app")
urlpatterns = [
    path('devicelist/', views.device_list , name="device-list"),
]