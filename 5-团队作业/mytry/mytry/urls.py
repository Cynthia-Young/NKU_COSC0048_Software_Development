
"""
URL configuration for mytry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from learn.views import index
from django.urls import path, include
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('captcha/', include('captcha.urls')),
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    # path('', include('userprofile.urls')),
    path('password_reset/', PasswordResetView.as_view(template_name='userprofile/password_reset_form.html',
                                                      email_template_name='userprofile/password_reset_email.html',),
         name='password_reset'),
    path('learn/', include('learn.urls')),  # 这里包含learn应用的URL配置
    path('SmartCenter/', include('SmartCenter.urls')),  
    path('DataCenter/', include('DataCenter.urls')),  
    path('BackManage/', include('BackManage.urls')),  
    path('MainInformation/', include('MainInformation.urls')),  
    path('UnderWater/', include('UnderWater.urls')),  

]
#设置静态文件路径
urlpatterns += staticfiles_urlpatterns()
