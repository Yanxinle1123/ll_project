from django.urls import path

from . import views

"""定义learning_logs的URL模式"""

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index')
]
