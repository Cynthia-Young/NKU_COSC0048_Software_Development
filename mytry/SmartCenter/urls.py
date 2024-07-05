

# learn/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('SmartCenter/', views.SmartCenter, name='SmartCenter'),  
    path('SmartCenter_user/', views.SmartCenter_user, name='SmartCenter_user'),  
        # 其他路由...
    path('update-fish/', views.update_fish_info, name='update_fish'),
]