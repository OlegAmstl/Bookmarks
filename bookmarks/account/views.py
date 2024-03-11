from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm


def user_login(request):
    """
    Представление входа в систему
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Аутентификация прошла успешно')
                else:
                    return HttpResponse('Аккаунт отключён')
            else:
                return HttpResponse('Неверный логин или пароль')
    else:
        form = LoginForm()
    return render(request,
                  'account/login.html', {'form': form})


def dashboard(request):
    """
    Доска сохраненного контента пользователя.
    :param request:
    :return: Отображает сохраненный контент в личном дашборде пользователя.
    """
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})
