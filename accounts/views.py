from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):
    """注册新用户"""
    if request.method == 'POST':
        # 显示表单数据
        form = UserCreationForm(request.POST)
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录
            login(request, new_user)
            return redirect('learning_logs:index')
    # 显示空表单
    context = {'form': form}
    return render(request, 'registration/register.html', context)
