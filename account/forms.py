from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class LoginForm(forms.Form):  # 用的request.POST参数传递
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)  # widget用于传递数据和设置外观


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email")  # 声明本表单所应用的数据模型，确定写入数据库的哪些记录里面

    def clean_password2(self):  # 调用表单实例对象的is_valid()方法时会执行
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords do not match.")
        return cd['password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone", "birth")

