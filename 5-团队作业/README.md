1. 在mytry/setting.py文件中修改数据库USER和PASSWORD信息

   ```
   DATABASES = {
       'default': {
           # 'ENGINE': 'django.db.backends.sqlite3',
           # 'NAME': BASE_DIR / 'db.sqlite3',
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'mytry',
           'USER': 'root',
           'PASSWORD': '123456', #修改密码
           'HOST': '127.0.0.1',
           'PORT': '3306',
       }
   }
   ```

2. 在终端执行如下语句即可创建数据库的迁移文件：

   ```
   python manage.py makemigrations
   ```

3. 然后执行如下命令进行数据库的初始化：

   ```
   python manage.py migrate
   ```

4. 将mytry目录下的BackManage_device.xlsx文件导入backmanage_device表格

   DataCenter-hardware.xlsx文件导入datacenter_hardwareinfo表格

   Fish.csv文件导入underwater_fish表格

   Smart_Env.xlsx文件导入smartcenter_environmentdata表格

   Smart_Fishdetected.xlsx文件导入smartcenter_fish_detect表格

5. 在终端执行如下语句启动项目：

   ```
   python manage.py runserver
   ```

   