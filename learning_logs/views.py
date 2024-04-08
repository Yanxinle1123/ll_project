from django.shortcuts import render


# 创建视图
def index(request):
    return render(request, 'learning_logs/index.html')
