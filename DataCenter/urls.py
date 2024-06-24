

# learn/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DataCenter, name='DataCenter'),
]