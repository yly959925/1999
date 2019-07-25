from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
import re
from user.models import User
# Create your views here.


# user/register/



def register(request):
    """注册"""
    # if request.method == "GET":
    return render(request,"register.html") #注册界面

def register_handle(request):

    #1 接收数据
    username = request.POST.get("user_name")
    password = request.POST.get("pwd")
    email = request.POST.get("email")
    allow = request.POST.get("allow")
    #2 数据校验
    if not all([username,password,email]):
        return render(request,"register.html",{"errmsg":"数据不完整"})

    if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

    if  allow != "on":
        return render(request,"register.html",{"errmsg":"请同意协议"})
    #3 进行业务处理  进行用户注册
    user = User.objects.create_user(username,password,email)

    #4 返回响应  跳转到首页
    return redirect(reverse("goods:index"))