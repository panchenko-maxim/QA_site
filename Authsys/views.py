from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


def test_view(request):
    return HttpResponse('<h1>Test</h1>')


@csrf_exempt
def sign_in(request):
    print(request.POST)
    if 'username' in request.POST:
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('/main/all_categories')
        else:
            return render(request, 'sign_in.html')
    else:
        return render(request, 'sign_in.html')


def log_out(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

