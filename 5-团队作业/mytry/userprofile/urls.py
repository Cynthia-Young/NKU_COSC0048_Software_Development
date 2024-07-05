from django.urls import path
from .views import *

app_name = 'userprofile'

urlpatterns = [
    path('login/', user_login, name='login'),
    # path('', user_login),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('profile/', user_profile, name='profile'),
]
