
# UnderWater/urls.py  
from django.urls import path  
from .views import generate_csv

from . import views  # 假设你的视图函数在 views.py 文件中  
  
urlpatterns = [  
    path('', views.UnderWater, name='UnderWater'),  # 空路径（即/learn/）将会调用learn应用的index视图 
    path('UnderWater_user/', views.UnderWater_user, name='UnderWater_user'),
    path('download-csv/', generate_csv, name='download-csv'),
    # path('fishnum/', views.FishNum, name='fishnum'),
    # path('fishnum/', views.FishNum, name='fishnum'),
    

]



# urlpatterns = [
#     path('upload-csv/', upload_csv, name='upload_csv'),
# ]