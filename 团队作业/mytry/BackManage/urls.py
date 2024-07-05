

# learn/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BackManage, name='BackManage'),  # 空路径（即/learn/）将会调用learn应用的index视图
    path('grant', views.Grant, name='Grant'),
]