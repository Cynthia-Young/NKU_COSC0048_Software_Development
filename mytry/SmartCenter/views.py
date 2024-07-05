from django.shortcuts import render
import requests
# Create your views here.

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import EnvironmentData
from .models import Fish_detect
from django.http import JsonResponse
def SmartCenter(request):
    # 天气部分
    api_key = '006d982064c569b6a16def3a5f704fdc'
    city_name = 'Tianjin'  # 可以替换为要查询的城市
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=zh_cn'
    response = requests.get(url)
    context = {}
    # 鱼群部分
        # 使用以下查询语句直接获取随机记录
    fish_info = Fish_detect.objects.order_by('?').first()
    # 环境部分
    latest_data = EnvironmentData.objects.latest('monitoring_date')# 获取最近的数据
    score = calculate_score(latest_data.water_quality, latest_data.dissolved_oxygen)# 计算得分
        # 预警逻辑
    WARNING_OXYGEN=7.0
    WARNING_TEMPREATURE=18.0
    warning_oxygen= '是' if latest_data.dissolved_oxygen < WARNING_OXYGEN else '否' #当溶解氧低于某个阈值
    warning_temperature= '是' if latest_data.water_temperature > WARNING_TEMPREATURE else '否' #当温度高于某个阈值
    if response.status_code == 200:
        weather_data = response.json()
        context = {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed'],

            'latest_data': latest_data,
            'score': score,
            'warning_oxygen': warning_oxygen,
            'warning_temperature': warning_temperature,

            # 'fish': fish_info,
            'fish': {
            'code': fish_info.code,
            'species': fish_info.species,
            'length': fish_info.length,
            'weight': fish_info.weight,
            }
        }
    else:
        context = {'error_message': '无法获取天气信息',
                   'latest_data': latest_data,
                    'score': score,
                    'warning_oxygen': warning_oxygen,
                    'warning_temperature': warning_temperature,

                    # 'fish': fish_info,
                    'fish': {
                        'code': fish_info.code,
                        'species': fish_info.species,
                        'length': fish_info.length,
                        'weight': fish_info.weight,
                    }
                    }

    return render(request, 'SmartCenter/trend.html', context)

    
#     return render(request, 'your_template_name.html', context={'fish': random_fish}) # 这里应返回一个包含新鱼信息的HTML片段或直接渲染整个页面
def SmartCenter_user(request):
    # 天气部分
    api_key = '006d982064c569b6a16def3a5f704fdc'
    city_name = 'Tianjin'  # 可以替换为要查询的城市
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=zh_cn'
    response = requests.get(url)
    context = {}
    # 鱼群部分
        # 使用以下查询语句直接获取随机记录
    fish_info = Fish_detect.objects.order_by('?').first()
    # 环境部分
    latest_data = EnvironmentData.objects.latest('monitoring_date')# 获取最近的数据
    score = calculate_score(latest_data.water_quality, latest_data.dissolved_oxygen)# 计算得分
        # 预警逻辑
    WARNING_OXYGEN=7.0
    WARNING_TEMPREATURE=18.0
    warning_oxygen= '是' if latest_data.dissolved_oxygen < WARNING_OXYGEN else '否' #当溶解氧低于某个阈值
    warning_temperature= '是' if latest_data.water_temperature > WARNING_TEMPREATURE else '否' #当温度高于某个阈值
    if response.status_code == 200:
        weather_data = response.json()
        context = {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed'],

            'latest_data': latest_data,
            'score': score,
            'warning_oxygen': warning_oxygen,
            'warning_temperature': warning_temperature,

            # 'fish': fish_info,
            'fish': {
            'code': fish_info.code,
            'species': fish_info.species,
            'length': fish_info.length,
            'weight': fish_info.weight,
            }
        }
    else:
        context = {'error_message': '无法获取天气信息',
                   'latest_data': latest_data,
                    'score': score,
                    'warning_oxygen': warning_oxygen,
                    'warning_temperature': warning_temperature,

                    # 'fish': fish_info,
                    'fish': {
                        'code': fish_info.code,
                        'species': fish_info.species,
                        'length': fish_info.length,
                        'weight': fish_info.weight,
                    }
                    }
    # context = {'title': 'My Page Title'}  # 数据字典
    # return render(request, '/templates/trend.html', context)  # 使用模板
    return render(request, 'SmartCenter/trendcopy.html', context)

def calculate_score(water_quality, dissolved_oxygen):
    # 假设的简单分数计算，实际情况可能更复杂
    base_score = 10
    if water_quality == 'Ⅰ':
        score = base_score + 5
    elif water_quality == 'Ⅱ':
        score = base_score
    elif water_quality == 'Ⅲ':
        score = base_score - 3
    elif water_quality == 'Ⅳ':
        score = base_score - 5
    else:
        score = base_score - 10
    
    # # 根据溶解氧调整分数
    # score += dissolved_oxygen / 10
    # 转化为百分制
    score = round((score / 15) * 100, 2)
    return score


def update_fish_info(request):
    """
    AJAX视图函数，用于提供新的随机鱼群数据。
    """
    fish_info = Fish_detect.objects.order_by('?').first()
    data = {
        'code': fish_info.code,
        'species': fish_info.species,
        'length': fish_info.length,
        'weight': fish_info.weight,
    }
    return JsonResponse(data)


