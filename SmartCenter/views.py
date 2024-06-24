from django.shortcuts import render

# Create your views here.


def SmartCenter(request):
    context = {'title': 'My Page Title'}  # 数据字典
    # return render(request, '/templates/trend.html', context)  # 使用模板
    return render(request, 'SmartCenter/trend.html', context)

def SmartCenter_user(request):
    context = {'title': 'My Page Title'}  # 数据字典
    # return render(request, '/templates/trend.html', context)  # 使用模板
    return render(request, 'SmartCenter/trendcopy.html', context)