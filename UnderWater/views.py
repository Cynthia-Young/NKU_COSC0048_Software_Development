
from django.shortcuts import render
# import csv
# from .forms import CSVUploadForm
from .models import Fish
# Create your views here.
from django.db.models import Count
from django.http import HttpResponse
import csv
def UnderWater(request):
    all_fish = Fish.objects.all()
    # 鱼群总量
    fishnum=Fish.objects.all().count()
    # 每一种鱼群的数量
    fish_counts=Fish.objects.values('Species').annotate(count=Count('Species'))
        # 将查询结果转换为ECharts所需的数据格式
    chart_data = [{"name": species['Species'], "value": species['count']} for species in fish_counts]
    # 用于画鱼群分布曲线
    bream_weights = Fish.objects.filter(Species='Bream').values_list('Weight', flat=True)
    roach_weights = Fish.objects.filter(Species='Roach').values_list('Weight', flat=True)
    whitefish_weights = Fish.objects.filter(Species='Whitefish').values_list('Weight', flat=True)
    parkki_weights = Fish.objects.filter(Species='Parkki').values_list('Weight', flat=True)
    perch_weights = Fish.objects.filter(Species='Perch').values_list('Weight', flat=True)
    pike_weights = Fish.objects.filter(Species='Pike').values_list('Weight', flat=True)
    smelt_weights = Fish.objects.filter(Species='Smelt').values_list('Weight', flat=True)

    context = {'all_fish': all_fish,
               'fishnum':fishnum,
               'fish_counts':fish_counts,
               "chart_data": chart_data,
                'Bream_weights': list(bream_weights),
                'Roach_weights': list(roach_weights),
                'Whitefish_weights': list(whitefish_weights),
                'Parkki_weights': list(parkki_weights),
                'Perch_weights': list(perch_weights),
                'Pike_weights': list(pike_weights),
                'Smelt_weights': list(smelt_weights),

               }
    return render(request, 'UnderWater/UnderWater.html', context)

def UnderWater_user(request):
    context = {'title': 'My Page Title'}  # 数据字典
    # return render(request, '/templates/trend.html', context)  # 使用模板
    return render(request, 'UnderWater/UnderWater_user.html', context)

def generate_csv(request):
    # 获取数据库中的数据
    data = Fish.objects.all()

    # 创建一个CSV文件
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="fish_data.csv"'

    # 写入CSV文件头部
    writer = csv.writer(response)
    writer.writerow(['Species', 'Weight', 'Length1', 'Length2','Length3','Height','Width'])
    for fish in data:
        writer.writerow([fish.Species, fish.Weight, fish.Length1, fish.Length2, fish.Length3, fish.Height, fish.Width])
    # 返回生成的CSV数据
    return response

