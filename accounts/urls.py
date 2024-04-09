from django.urls import path, include

"""为Django应用程序accounts定义URL模式"""

app_name = 'accounts'
urlpatterns = [
    # 用户登录
    path('', include('django.contrib.auth.urls'))
]
