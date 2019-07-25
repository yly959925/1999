from django.conf.urls import url

from apps.user import views
# from apps.user.views import RegisterView
app_name='apps.user'




urlpatterns=[
    url(r'^register/$',views.register,name='register'), # 注册页面
    url(r'^register_handle$',views.register_handle,name='register_handle'), #注册管理
]