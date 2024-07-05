# 引入modelform组件
from django import forms
from django.core.validators import ValidationError, RegexValidator

from app01 import models
from app01.utils.encrypt import md5


class loginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    def clean_password(self):
        pwd = self.cleaned_data['password']
        return md5(pwd)
class BootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs = {'class': 'form-control'}

class UserModelForm(BootstrapForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'depart', 'gender']



class PrettyModelForm(BootstrapForm):
    # 校验:  方式1  通过正则表达式验证手机号码的格式
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机格式错误')],
    )

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    # 校验 方式2  通过在钩子函数里面添加逻辑来验证
    def clean_mobile(self):
        # 返回用户输入数据
        tx_mobile = self.cleaned_data['mobile']
        # 编辑状态下就是验证除了自己外还存在相同的手机号码
        exist = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=tx_mobile).exists()
        # 如果是新增状态下就是如下的代码来检测是否存在相同的手机号码
        # exist = models.PrettyNum.objects.filter(mobile=tx_mobile).exists()
    #     # 验证
        if exist:
            # 验证失败
            raise ValidationError("手机号已存在")
        # 验证通过,用户输入的值返回
        return tx_mobile

class AdminModelForm(BootstrapForm):
    # 给新增管理员页面增加确认密码字段
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True),
    )
    class Meta:
        model = models.Admin
        fields = ['username', 'password', 'confirm_password']
        # 把密码输入框由文本输入框改为密码输入框
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

    # 密码加密存储到数据库
    def clean_password(self):
        pwd = self.cleaned_data['password']
        return md5(pwd)

    def clean_confirm_password(self):
        # print(self.cleaned_data)
        pwd = self.cleaned_data['password']
        confirm = md5(self.cleaned_data['confirm_password'])
        if pwd != confirm:
            raise ValidationError("密码不一致")
        return confirm


