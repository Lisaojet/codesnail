# qrcodeapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.qrcodeapp, name='qrcodeapp'),
]
