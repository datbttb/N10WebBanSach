from django import template
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
def displayCustomerInfo(request):
    user = User.objects.get(username='datbttb')

    template = loader.get_template('profile.html')
    context = {
        'user': user,
    }
    return HttpResponse(template.render(context, request))


def loginForm(request):
    return render(request=request, template_name='login.html')


def registerForm(request):
    return render(request=request, template_name='register.html')


# các hàm xử lý

# hàm đăng nhập
def doLogin(request):
    # if request.user.is_authenticated:
    #     return redirect('https://www.youtube.com/')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    # user = User.objects.is_authenticated(username = username, password = password)
    # user = authenticate(request, username=username, password=password)
    if user is not None:
        # login(request, user)
        return redirect('https://www.youtube.com/')  # profile
    else:
        # 11/03/2023 chưa xử lý xong, sẽ phải hiện ra thông báo nhập sai mật khẩu
        messages.info(request, 'Nhập sai tài khoản hoặc mật khẩu!')
        # msg = 'Error Login'
        # form = AuthenticationForm(request.POST)
        return redirect('https://www.facebook.com/')
        # return render(request, 'login.html', {'form': form, 'msg': msg})


# xử lý việc quên mật khẩu
def forgotPassword(request):
    return render(request, 'ResetPassword.html')


# hàm đăng ký
def registerUser(request, template_name="register.html"):
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    fullName = firstName + lastName
    username = request.POST['username']
    password = request.POST['password']
    address = request.POST['address']
    email = request.POST['email']
    phoneNumber = request.POST['phonenumber']
    # newUser = User(username = username, password = password, fullName = fullName, address = address, email = email, phonenum = phoneNumber)

    # newUser.save()
    user = User.objects.create_user(username=username, email=email, password=password, first_name=firstName,
                                    last_name=lastName)
    print(request.POST['username'])
    print(request.POST)
    user.save()
    # admin.site.register(user)
    # logging.debug("Nothing to do here")
    return redirect('/')





