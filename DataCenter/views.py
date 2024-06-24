from django.shortcuts import render

# Create your views here.

def DataCenter(request):
    context = {'title': 'My Page Title'}  # 数据字典
    # return render(request, '/templates/trend.html', context)  # 使用模板
    return render(request, 'DataCenter/NCDindex.html', context)