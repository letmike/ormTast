from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from app01.models import User


# 注册
class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        error = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        if password != re_password:
            error = '两次密码不一致'
            return render(request, 'register.html', locals())

        if User.objects.filter(username=username):
            error = '用户名已存在'
            return render(request, 'register.html', locals())

        User.objects.create(username=username, password=password)
        return redirect('login')


# 首页
class Index(View):
    def get(self, request):
        user_list = User.objects.all()
        count = User.objects.count()
        return render(request, 'index.html', locals())


# 登录
class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        error = ""
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()

        if not user:
            error = '用户名或者密码错误'
            return render(request, 'login.html', locals())

        return redirect("index")

class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')