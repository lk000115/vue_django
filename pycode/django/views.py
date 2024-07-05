from django.shortcuts import render, redirect

from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.forms import UserModelForm,PrettyModelForm,AdminModelForm,loginForm


# Create your views here.
def admin_list(request):
    # models.Admin.objects.create(username='s0008',password='123')
    queryset = models.Admin.objects.all()
    return render(request,'admin_list.html',{'queryset':queryset})

def admin_add(request):
    # 用修改数据的公共模板change.html,传入title参数
    title = '新建管理员'
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request,'change.html',{'title':title,'form':form})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request,'change.html',{'title':title,'form':form})

def admin_edit(request,nid):
    title = '编辑管理员'
    row_obj= models.Admin.objects.filter(id=nid)
    if not row_obj:
        return redirect('/admin/list/')
    if request.method == 'GET':
        form = AdminModelForm(instance=row_obj)
        return render(request,'change.html',{'title':title,'form':form})
    form = AdminModelForm(data=request.POST,instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request,'change.html',{'title':title,'form':form})

def admin_delete(request,nid):
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list/')

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

    #----------------------------------------------------------
    # 根据用户的页码计算页码起止位置
    # page = int(request.GET.get('page',1))
    # page_size = 10
    # start = (page - 1) * page_size
    # end = page*page_size
    #
    # queryset = queryset[start:end]
    # # 页码总条数
    # total_count = models.PrettyNum.objects.filter(**data_dict).count()
    # # 计算总页码
    # total_page_count,div = divmod(total_count,page_size)
    # if div:
    #     total_page_count += 1
    #
    # # 显示当前页的前5页,后5页
    # plus = 5
    #
    # # 以下逻辑放在类的方法html中
    # if total_page_count <= 2*plus +1 :
    #     start_page = 1
    #     end_page = total_page_count
    # else:
    #     # 当前页< 5
    #     if page <= plus:
    #         start_page = 1
    #         end_page = page + plus +1
    #     else:
    #         # 当前页 > 5
    #         if (page + plus) > total_page_count:
    #             start_page = total_page_count - 2*plus
    #             end_page = total_page_count
    #         else:
    #             start_page = page - plus
    #             end_page = page + plus +1
    #
    # page_str_list = []
    # # 上一页
    # if page > 1:
    #     prev = '<li ><a class="page-link" href="?page={}">上一页</a></li>'.format(page-1)
    # else:
    #     prev = '<li ><a class="page-link" href="?page={}">上一页</a></li>'.format(1)
    # page_str_list.append(prev)
    # for i in range(start_page,end_page):
    #     if i == page:
    #         ele = '<li class="page-item active"><a class="page-link" href="?page={}">{}</a></li>'.format(i,i)
    #     else:
    #         ele = '<li ><a class="page-link" href="?page={}">{}</a></li>'.format(i,i)
    #     page_str_list.append(ele)
    #
    # # 下一页
    # if page < total_page_count:
    #     prev = '<li ><a class="page-link" href="?page={}">下一页</a></li>'.format(page + 1)
    # else:
    #     prev = '<li ><a class="page-link" href="?page={}">下一页</a></li>'.format(total_page_count)
    # page_str_list.append(prev)
    #
    # # 必须把字符串转为安全的数据才能传给前端生成HTML
    # page_str = mark_safe(''.join(page_str_list))

    page_object = Pagination(request,queryset)
    page_queryset = page_object.page_queryset
    page_str = page_object.html()
    context = {
        'queryset': page_queryset,
        "page_str": page_str,
        "search_data": search_data,
    }
    return render(request, 'pretty_list.html', context)

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

def login(request):
    if request.method == 'GET':
        form = loginForm()
        return render(request, 'login.html',{'form':form})
    form = loginForm(data=request.POST)
    if form.is_valid():
        pwd_obj = models.Admin.objects.filter(**form.cleaned_data).first()
        # r如果数据库不存在此用户名,密码,抛出异常
        if not pwd_obj:
            form.add_error('password','用户名或密码错误')
            return render(request, 'login.html', {'form':form})
        # 如果用户名,密码正确
        # 网站生成随机字符串,给用户写道浏览器的cookies中.同时session保存一份
        request.session["info"] = {'id':pwd_obj.id,'name':pwd_obj.username}
        return redirect('/admin/list/')

    return render(request, 'login.html', {'form':form})