from django.shortcuts import render, redirect
from app01 import models
# 引入modelform组件
from django import forms
from django.core.validators import ValidationError, RegexValidator

from app01.models import UserInfo


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'depart', 'gender']

    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control'}


class PrettyModelForm(forms.ModelForm):
    # 校验:  方式1  通过正则表达式验证手机号码的格式
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机格式错误')],
    )

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    def __init__(self, *args, **kwargs):
        super(PrettyModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control'}

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


# Create your views here.
def depart_list(request):
    """部门列表页面"""
    queryset = models.Department.objects.all()
    return render(request, 'depart_list.html', {'queryset': queryset})


def depart_add(request):
    """添加部门"""
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    title = request.POST.get('title')
    models.Department.objects.create(title=title)
    return redirect(depart_list)


def depart_del(request):
    """删除部门"""
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect(depart_list)


def depart_edit(request, nid):
    """编辑部门"""
    if request.method == 'GET':
        row_obj = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {'row_obj': row_obj})
    title = request.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect(depart_list)


def user_list(request):
    """用户列表页面"""
    queryset = models.UserInfo.objects.all()
    return render(request, 'user_list.html', {'queryset': queryset})


def user_add(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_add.html', {'form': form})
        # 获取提交的表单，并把数据传给form
    form = UserModelForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_add.html', {'form': form})


def user_edit(request, nid):
    # 编辑员工资料
    row_obj = models.UserInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        # 如果是get请求,就把获取的当前行数据传递给form,展示在修改员工页面
        form = UserModelForm(instance=row_obj)
        return render(request, 'user_edit.html', {'form': form})
    # 如果是提交的POST请求,就把传递给form,并传递给instance说明是修改当前数据
    form = UserModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {'form': form})


def user_delete(request, nid):
    # 删除员工
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')


def pretty_list(request):
    """靓号列表"""
    # for i in range(100):
    #     t = 13559900020
    #     t = t + i
    #     t = str(t)
    #     models.PrettyNum.objects.create(mobile=t,price=1000,level=1,status=2)
        # print(type(t))
    data_dict = {}
    search_data = request.GET.get('q',"")
    if search_data is not None:
        data_dict["mobile__contains"] = search_data
    queryset = models.PrettyNum.objects.filter(**data_dict).order_by("-level")
    return render(request, 'pretty_list.html', {'queryset': queryset,"search_data":search_data})

# 新增靓号
def pretty_add(request):
    if request.method == 'GET':
        form = PrettyModelForm()
        return render(request, 'pretty_add.html', {'form': form})
    form = PrettyModelForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    return render(request, 'pretty_add.html', {'form': form})

# 编辑靓号
def pretty_edit(request, nid):
    row_obj = models.PrettyNum.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = PrettyModelForm(instance=row_obj)
        return render(request, 'pretty_edit.html', {'form': form})
    form = PrettyModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    return render(request, 'pretty_edit.html', {'form': form})