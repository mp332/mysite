from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path

app_name = 'account'

urlpatterns = [
    # url(r'^login/$', views.user_login, name="user_login"),    # 自定义登录
    # url(r'^login/$', auth_views.auth_login, name='user_login')  # django内置登录
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name="user_login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name="user_logout"),
    url(r'^register/$', views.register, name="user_register"),
]
