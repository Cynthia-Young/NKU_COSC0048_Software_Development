from django.shortcuts import render
import pandas as pd
from .models import Water
import sys
sys.path.append('../')
from BackManage.models import Device

# Create your views here.

WARNING_OXYGEN=7.0
WARNING_TEMPREATURE=18.0


def calculate_warnings(water):
    warning_oxygen = '是' if water.dissolved_oxygen < WARNING_OXYGEN else '否'
    warning_temperature = '是' if water.temperature > WARNING_TEMPREATURE else '否'
    warning = 1 if warning_oxygen == '是' or warning_temperature == '是' else 0
    return warning_oxygen, warning_temperature, warning



def get_water_data():
    today = pd.Timestamp.now().strftime('%Y-%m-%d')
    try:
        water = Water.objects.get(time__startswith=today)
    except Water.DoesNotExist:
        try:
            water = Water.objects.get(time__startswith='2024-06-22')
        except Water.DoesNotExist:
            water = None
    return water

def get_device_status():
    try:
        device = Device.objects.filter(type__contains='摄像头', on=0)
        on = 0 if device else 1
    except:
        on = 0

    try:
        device = Device.objects.filter(type__contains='摄像头', state__in=[1, 2])
        abn = '存在异常设备' if device else '状态均良好'
    except:
        abn = '状态均良好'

    return on, abn

def prepare_context(water):
    if water:
        warning_oxygen, warning_temperature, warning = calculate_warnings(water)
    else:
        warning_oxygen, warning_temperature, warning = '否', '否', 0

    all_water = Water.objects.all().order_by('-time')
    water_num = all_water.count()
    if not all_water:
        all_water = None
    if not water:
        water = None
        warning_oxygen = '无'
        warning_temperature = '无'

    on, abn = get_device_status()

    context = {
        'today_water': water,
        'all_water': all_water,
        'water_num': water_num,
        'warning_oxygen': warning_oxygen,
        'warning_temperature': warning_temperature,
        'on': on,
        'abn': abn,
        'warning': warning
    }
    return context

def MainInformation(request):
    water = get_water_data()
    context = prepare_context(water)
    return render(request, 'MainInformation/MainInformation.html', context)

def MainInformation_user(request):
    water = get_water_data()
    context = prepare_context(water)
    return render(request, 'MainInformation/MainInformation_user.html', context)



def insert_water_data(time, water_type, temperature, ph, dissolved_oxygen, conductivity, 
                      turbidity, permanganate_index, ammonia_nitrogen, total_phosphorus, total_nitrogen):
    Water.objects.create(time=time, type=water_type, temperature=temperature, 
                         ph=ph, dissolved_oxygen=dissolved_oxygen, conductivity=conductivity, 
                         turbidity=turbidity, permanganate_index=permanganate_index, 
                         ammonia_nitrogen=ammonia_nitrogen, total_phosphorus=total_phosphorus, 
                         total_nitrogen=total_nitrogen)
    



def clear_water_data():
    # 删除Water表中的所有记录
    Water.objects.all().delete()
    print("水质数据表已清空。")


def Upload(request, isUser=False):
    if request.method == 'POST'and len(request.FILES) > 0:
        f = request.FILES['file']
        excel_type = f.name.split('.')[1]
        if excel_type in ['xlsx', 'xls']:
            clear_water_data()
            data = pd.read_excel(f,
                                 date_format=lambda x: pd.to_datetime(x, format="%Y/%m/%d")
)
            times = pd.to_datetime(data.iloc[:,0]).dt.date
            for i in range(len(data)):
                # time = data.iloc[i,0]
                time = times.iloc[i]
                water_type = data.iloc[i,1]
                temperature = data.iloc[i,2]
                ph = data.iloc[i,3]
                dissolved_oxygen = data.iloc[i,4]
                conductivity = data.iloc[i,5]
                turbidity = data.iloc[i,6]
                permanganate_index = data.iloc[i,7]
                ammonia_nitrogen = data.iloc[i,8]
                total_phosphorus = data.iloc[i,9]
                total_nitrogen = data.iloc[i,10]
                insert_water_data(time, water_type, temperature, ph, dissolved_oxygen, conductivity, 
                                  turbidity, permanganate_index, ammonia_nitrogen, total_phosphorus, total_nitrogen)
        else:
            error = '上传文件类型错误！'
            print(error)
        print('上传成功！')
    if isUser:
        return render(request, 'MainInformation/MainInformation_user.html')
    else:
        return render(request, 'MainInformation/MainInformation.html')


def on_off(request, isUser=False):
    if request.method == 'POST':
        on = request.POST.get('on-off')
        if on == '1':
            device = Device.objects.filter(type__contains='摄像头', on=1)
            if device:
                device.update(on=0)
        else:
            device = Device.objects.filter(type__contains='摄像头', on=0)
            if device:
                device.update(on=1)
    if isUser:
        return render(request, 'MainInformation/MainInformation_user.html')
    else:
        return render(request, 'MainInformation/MainInformation.html')

