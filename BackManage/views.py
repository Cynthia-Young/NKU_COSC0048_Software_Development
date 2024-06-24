from django.shortcuts import render
#from .DataViews import ShowUser
from .models import Device
import sys
sys.path.append('../')
from userprofile.models import UserProfile

# Create your views here.


def BackManage(request):
    username0 = request.session.get('username', None)
    print(username0)
    users = UserProfile.objects.exclude(username=username0)  # 获取所有用户信息，排除特定用户
    devices = Device.objects.all()  # 获取所有设备信息
    for device in devices:
        if device.state == 0:
            device.status = '正常'
        elif device.state == 1:
            device.status = '故障'
        else:
            device.status = '未知'
    context = {'users': users, 'devices': devices}  # 数据字典
    return render(request, 'BackManage/chronic.html', context)


def Grant(request):
    if request.method == 'POST' and len(request.POST) > 0:
        id = request.POST.get('id')
        print(id)
        now_user = UserProfile.objects.get(id=id)
        now_user.is_staff = not now_user.is_staff
        now_user.is_superuser = not now_user.is_superuser
        now_user.save()
    return render(request, 'teacher_page/index2.html')